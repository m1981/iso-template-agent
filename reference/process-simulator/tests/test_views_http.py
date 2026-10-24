import concurrent.futures
import http.client
import json
import threading
import unittest

from app.projections import project
from app.server import make_server
from app.session import export_session
from test_engine import TO_DEMO, walk


class ViewContract(unittest.TestCase):
    def test_reverse_links_include_the_exact_historical_revision(self):
        view = project(walk(*TO_DEMO))
        cards = {c["key"]: c for c in view["cards"]}
        self.assertIn("RUN1@1", [r["key"] for r in cards["CODE1@1"]["used_by"]])
        self.assertNotIn("RUN2@1", [r["key"] for r in cards["CODE1@1"]["used_by"]])
        self.assertIn("RUN2@1", [r["key"] for r in cards["CODE1@2"]["used_by"]])
        self.assertFalse(view["accepted"])
        self.assertFalse(view["release_ready"])
        self.assertTrue(view["simulated"])

    def test_history_is_read_only_and_projection_contains_no_future_results(self):
        view = project(walk(*TO_DEMO), cursor=5)
        self.assertTrue(view["read_only"])
        self.assertFalse(any(c["id"] == "RUN1" for c in view["cards"]))
        self.assertTrue(all(not a["enabled"] for a in view["actions"]))
        self.assertEqual(len(view["history"]), 11)


class HTTPContract(unittest.TestCase):
    def setUp(self):
        self.server = make_server()
        self.worker = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.worker.start()
        self.port = self.server.server_port

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.worker.join(timeout=2)

    def request(self, method, path, payload=None, raw=None, headers=None):
        conn = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        body = raw if raw is not None else json.dumps(payload) if payload is not None else None
        conn.request(method, path, body, headers or {"Content-Type": "application/json"})
        response = conn.getresponse()
        body = response.read().decode()
        status = response.status
        mime = response.getheader("Content-Type", "")
        conn.close()
        return status, json.loads(body) if "application/json" in mime else body

    def test_command_and_duplicate_are_atomic(self):
        status, initial = self.request("GET", "/api/state")
        self.assertEqual(status, 200)
        status, view = self.request("POST", "/api/command", {"action": "scope", "note": "", "version": initial["version"]})
        self.assertEqual(status, 200)
        self.assertEqual(view["cursor"], 1)
        status, refusal = self.request("POST", "/api/command", {"action": "scope", "note": "", "version": view["version"]})
        self.assertEqual(status, 409)
        self.assertIn("error", refusal)
        self.assertEqual(self.request("GET", "/api/state")[1], view)

    def test_two_competing_commands_do_not_overwrite_state(self):
        payload = {"action": "scope", "note": "", "version": 0}
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            results = list(executor.map(lambda _: self.request("POST", "/api/command", payload), range(2)))
        self.assertEqual(sorted(status for status, _ in results), [200, 409])
        self.assertEqual(self.request("GET", "/api/state")[1]["cursor"], 1)

    def test_import_replays_and_history_cannot_be_edited(self):
        saved = export_session(walk(*TO_DEMO), 5)
        status, view = self.request("POST", "/api/import", {"session": saved, "version": 0})
        self.assertEqual(status, 200)
        self.assertTrue(view["read_only"])
        status, _ = self.request("POST", "/api/command", {"action": "red", "note": "", "version": view["version"]})
        self.assertEqual(status, 409)
        self.assertEqual(self.request("GET", "/api/export"), (200, saved))
        status, _ = self.request("POST", "/api/import", {"session": saved | {"lesson_version": 99}, "version": view["version"]})
        self.assertEqual(status, 409)
        self.assertEqual(self.request("GET", "/api/export"), (200, saved))
        status, current = self.request("POST", "/api/cursor", {"cursor": 11, "version": view["version"]})
        self.assertEqual(status, 200)
        self.assertFalse(current["read_only"])

    def test_bad_json_unknown_fields_and_paths_do_not_change_session(self):
        for raw in ('{', '{"version":0,"version":1}', 'NaN', '[]'):
            with self.subTest(raw=raw):
                status, _ = self.request("POST", "/api/command", raw=raw)
                self.assertEqual(status, 400)
        status, _ = self.request("POST", "/api/command", {"action": "scope", "note": "", "version": 0, "pass": True})
        self.assertEqual(status, 400)
        self.assertEqual(self.request("GET", "/api/export")[1]["commands"], [])
        self.assertEqual(self.request("GET", "/../collaboration.md")[0], 404)

    def test_long_but_valid_export_can_be_imported(self):
        from app.engine import transition
        state = walk(*TO_DEMO)
        for _ in range(40):
            state = transition(state, "reject", "Opis " * 400)
            state = transition(state, "clarify", "Treść" * 400)
            state = transition(state, "demo")
        saved = export_session(state)
        self.assertGreater(len(json.dumps(saved)), 131072)
        status, _ = self.request("POST", "/api/import", {"session": saved, "version": 0})
        self.assertEqual(status, 200)
        self.assertEqual(self.request("GET", "/api/export"), (200, saved))

    def test_local_static_assets_and_cross_origin_rejection(self):
        for path in ('/', '/style.css', '/main.js'):
            self.assertEqual(self.request("GET", path)[0], 200)
        status, _ = self.request("POST", "/api/command", {"action": "scope", "note": "", "version": 0},
                                 headers={"Content-Type": "application/json", "Origin": "https://example.invalid"})
        self.assertEqual(status, 403)
