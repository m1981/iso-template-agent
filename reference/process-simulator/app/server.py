"""Loopback-only HTTP adapter for one shared educational session."""
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock

from app.engine import Refused, initial_state, transition
from app.projections import project
from app.session import export_session, import_session, valid_cursor

STATIC = Path(__file__).resolve().parent / "static"
ASSETS = {"/": ("index.html", "text/html"), "/main.js": ("main.js", "text/javascript"),
          "/style.css": ("style.css", "text/css")}
MAX_BODY = 2 * 1024 * 1024


class BadRequest(ValueError):
    pass


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise BadRequest("JSON zawiera powtórzone pole.")
        result[key] = value
    return result


def reject_constant(value):
    raise BadRequest("JSON zawiera niedozwoloną stałą.")


class SessionStore:
    """Only mutable boundary; callers hold the lock for read/check/replace."""
    def __init__(self):
        self.state = initial_state()
        self.cursor = 0
        self.version = 0
        self.lock = Lock()

    def view(self):
        return project(self.state, self.cursor, self.version)

    def apply(self, path, payload):
        fields = {"/api/command": {"action", "note", "version"},
                  "/api/cursor": {"cursor", "version"},
                  "/api/import": {"session", "version"}}
        if type(payload) is not dict or set(payload) != fields[path]:
            raise BadRequest("Nieprawidłowe pola żądania.")
        if type(payload["version"]) is not int or payload["version"] != self.version:
            raise Refused("Widok jest nieaktualny. Odśwież stan przed kolejnym działaniem.")
        state, cursor = self.state, self.cursor
        if path == "/api/command":
            if cursor != len(state.events):
                raise Refused("Historia jest tylko do odczytu. Wróć do bieżącego kroku.")
            state = transition(state, payload["action"], payload["note"])
            cursor = len(state.events)
        elif path == "/api/cursor":
            valid_cursor(payload["cursor"], len(state.events))
            cursor = payload["cursor"]
        else:
            state, cursor = import_session(payload["session"])
        self.state, self.cursor = state, cursor
        self.version += 1
        return self.view()


class Handler(BaseHTTPRequestHandler):
    server_version = "ProcessLesson/1"

    def setup(self):
        super().setup()
        self.connection.settimeout(10)

    def log_message(self, format, *args):
        # No lesson contents or personal acceptance notes in server access logs.
        pass

    def send(self, status, body, mime="application/json"):
        encoded = json.dumps(body, ensure_ascii=False).encode() if mime == "application/json" else body
        self.send_response(status)
        self.send_header("Content-Type", mime + "; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(encoded)

    def local_request(self):
        port = self.server.server_port
        hosts = {f"127.0.0.1:{port}", f"localhost:{port}"}
        host = self.headers.get("Host")
        origin = self.headers.get("Origin")
        if host not in hosts or (origin is not None and origin != f"http://{host}"):
            self.send(403, {"error": "Serwer obsługuje tylko swój lokalny adres i origin."})
            return False
        return True

    def do_GET(self):
        if not self.local_request():
            return
        if self.path in ASSETS:
            filename, mime = ASSETS[self.path]
            self.send(200, (STATIC / filename).read_bytes(), mime)
        elif self.path in {"/api/state", "/api/export"}:
            with self.server.store.lock:
                store = self.server.store
                result = store.view() if self.path == "/api/state" else export_session(store.state, store.cursor)
            self.send(200, result)
        else:
            self.send(404, {"error": "Nieznana ścieżka."})

    def do_POST(self):
        if not self.local_request():
            return
        if self.path not in {"/api/command", "/api/cursor", "/api/import"}:
            self.send(404, {"error": "Nieznana ścieżka."})
            return
        try:
            if self.headers.get_content_type() != "application/json":
                raise BadRequest("Wymagany Content-Type: application/json.")
            if self.headers.get("Transfer-Encoding"):
                raise BadRequest("Wymagany pojedynczy JSON z Content-Length.")
            try:
                length = int(self.headers.get("Content-Length", "-1"))
            except ValueError as error:
                raise BadRequest("Nieprawidłowa długość żądania.") from error
            if not 0 < length <= MAX_BODY:
                raise BadRequest("Żądanie musi mieć od 1 do 2097152 bajtów.")
            data = self.rfile.read(length)
            if len(data) != length:
                raise BadRequest("Niepełne żądanie.")
            payload = json.loads(data, object_pairs_hook=unique_object, parse_constant=reject_constant)
            with self.server.store.lock:
                result = self.server.store.apply(self.path, payload)
            self.send(200, result)
        except (BadRequest, json.JSONDecodeError, UnicodeDecodeError, RecursionError) as error:
            self.send(400, {"error": str(error)})
        except Refused as error:
            self.send(409, {"error": str(error)})


def make_server(port=0):
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    server.store = SessionStore()
    return server


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    with make_server(args.port) as server:
        print(f"Lekcja: http://127.0.0.1:{server.server_port} — Ctrl+C kończy serwer.", flush=True)
        print("Jedna sesja w pamięci. Wyeksportuj ją przed zamknięciem serwera.", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
