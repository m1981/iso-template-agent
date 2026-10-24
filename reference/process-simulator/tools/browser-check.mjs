/** Real UI smoke/acceptance test. No packages; Node 22+ and installed Chrome.
 * Uses a new temporary profile and its own loopback Python server only.
 * Never connects to an existing browser or a user's browsing profile.
 */
import assert from 'node:assert/strict';
import {spawn} from 'node:child_process';
import {mkdtemp, mkdir, writeFile, rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {fileURLToPath} from 'node:url';
import path from 'node:path';

const root = fileURLToPath(new URL('../', import.meta.url));
const evidence = path.join(root, 'evidence');
const chromeBin = process.env.CHROME_BIN || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const python = process.env.PYTHON || 'python3';
const transcript = [];
const record = message => { transcript.push(message); console.log(message); };
const pause = ms => new Promise(resolve => setTimeout(resolve, ms));
const profile = await mkdtemp(path.join(tmpdir(), 'process-lesson-browser-'));
await mkdir(evidence, {recursive: true});
let chrome, server, socket, session;
let sequence = 0;
const pending = new Map();
async function stop(child) {
  if (!child || child.exitCode !== null) return;
  child.kill('SIGTERM');
  for (let i = 0; i < 40 && child.exitCode === null; i++) await pause(50);
  if (child.exitCode === null) child.kill('SIGKILL');
}
async function endpoint(child, pattern) {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error('Process endpoint timeout')), 15000);
    let text = '';
    const receive = chunk => {
      text += chunk.toString(); const match = text.match(pattern);
      if (match) { clearTimeout(timer); resolve(match[0]); }
    };
    child.stdout.on('data', receive); child.stderr.on('data', receive);
    child.once('error', error => { clearTimeout(timer); reject(error); });
    child.once('exit', code => { clearTimeout(timer); reject(new Error(`Process ended: ${code}. ${text}`)); });
  });
}
async function startServer() {
  server = spawn(python, ['-B', '-m', 'app.server', '--port', '0'], {cwd: root, stdio: ['ignore', 'pipe', 'pipe']});
  return endpoint(server, /http:\/\/127\.0\.0\.1:\d+/);
}
function cdp(method, params = {}, target = session) {
  return new Promise((resolve, reject) => {
    const id = ++sequence;
    const timer = setTimeout(() => { pending.delete(id); reject(new Error(`CDP timeout: ${method}`)); }, 15000);
    pending.set(id, {resolve, reject, timer});
    socket.send(JSON.stringify({id, method, params, ...(target ? {sessionId: target} : {})}));
  });
}
async function dom(source) {
  const result = await cdp('Runtime.evaluate', {expression: source, returnByValue: true, awaitPromise: true, userGesture: true});
  if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
  return result.result.value;
}
async function wait(source) {
  const deadline = Date.now() + 10000;
  while (Date.now() < deadline) {
    if (await dom(source)) return;
    await pause(40);
  }
  throw new Error(`DOM condition timed out: ${source}\n${await dom('document.body.innerText')}`);
}
async function click(text) {
  await dom(`(() => { const nodes = [...document.querySelectorAll('button')].filter(n => n.textContent.trim() === ${JSON.stringify(text)}); if (nodes.length !== 1 || nodes[0].disabled) throw new Error('Button unavailable: ' + ${JSON.stringify(text)}); nodes[0].click(); })()`);
}
async function fill(id, text) {
  await dom(`(() => { const node = document.getElementById(${JSON.stringify(id)}); node.value = ${JSON.stringify(text)}; node.dispatchEvent(new Event('input', {bubbles:true})); })()`);
}
async function step(text, number) {
  await click(text);
  await wait(`document.querySelector('#counters .metric strong')?.textContent === '${number}'`);
  assert.equal(await dom("document.getElementById('message').textContent"), '');
  record(`PASS step ${number}: ${text}`);
}
async function decision(text, note, number) {
  await click(text);
  await wait("document.getElementById('action-dialog').open");
  await fill('note', note);
  await click('Zapisz w fabule');
  await wait(`document.querySelector('#counters .metric strong')?.textContent === '${number}'`);
  record(`PASS step ${number}: ${text}`);
}
async function screenshot(name) {
  const {data} = await cdp('Page.captureScreenshot', {format: 'png', captureBeyondViewport: false});
  await writeFile(path.join(evidence, name), Buffer.from(data, 'base64'));
}
async function saveSession() {
  await click('Zapisz sesję'); await wait("document.getElementById('save-dialog').open");
  const value = await dom("document.getElementById('saved-json').value");
  await click('Zamknij zapis'); return JSON.parse(value);
}
try {
  record(`Browser trial ${new Date().toISOString()}; Node ${process.version}. Own server, synthetic lesson only.`);
  const url = await startServer();
  chrome = spawn(chromeBin, ['--headless=new', '--remote-debugging-port=0', '--remote-debugging-address=127.0.0.1',
    `--user-data-dir=${profile}`, '--no-first-run', '--no-default-browser-check', '--disable-background-networking',
    '--disable-component-update', '--disable-sync', '--disable-features=MediaRouter,OptimizationHints',
    '--metrics-recording-only', 'about:blank'], {stdio: ['ignore', 'pipe', 'pipe']});
  const wsURL = await endpoint(chrome, /ws:\/\/127\.0\.0\.1:\d+\/devtools\/browser\/[a-f0-9-]+/);
  socket = new WebSocket(wsURL);
  await new Promise((resolve, reject) => { socket.addEventListener('open', resolve, {once:true}); socket.addEventListener('error', reject, {once:true}); });
  socket.addEventListener('message', event => {
    const message = JSON.parse(event.data), item = pending.get(message.id);
    if (!item) return;
    clearTimeout(item.timer); pending.delete(message.id);
    if (message.error) item.reject(new Error(JSON.stringify(message.error))); else item.resolve(message.result);
  });
  record(`Browser: ${(await cdp('Browser.getVersion', {}, null)).product}`);
  const target = await cdp('Target.createTarget', {url: 'about:blank'}, null);
  session = (await cdp('Target.attachToTarget', {targetId: target.targetId, flatten: true}, null)).sessionId;
  await cdp('Page.enable'); await cdp('Runtime.enable');
  await cdp('Emulation.setDeviceMetricsOverride', {width:1440, height:1100, deviceScaleFactor:1, mobile:false});
  await cdp('Page.navigate', {url});
  await wait("document.getElementById('now')?.textContent === 'Uzgodnij zakres w fabule'");
  const blank = await saveSession(); assert.equal(blank.commands.length, 0);
  await screenshot('browser-00-start.png');
  const before = ['Uzgodnij zakres w fabule','Przygotuj plan I1','Zaprojektuj kontrakty C1/C2','Przejrzyj wymagania i projekt','Przygotuj przypadki T1–T5'];
  for (let i = 0; i < before.length; i++) await step(before[i], i + 1);
  assert.equal(await dom("document.querySelectorAll('#counters .metric strong')[2].textContent"), '0');
  record('PASS: five test cases exist, zero test executions.');
  await step('Uruchom próbę na szkielecie', 6);
  assert.match(await dom("document.getElementById('card').innerText"), /FAIL/);
  await screenshot('browser-06-red.png');
  await step('Zaimplementuj obliczenie', 7);
  assert.equal(await dom("document.getElementById('element').value"), 'CODE1@2');
  await step('Ponów testy jednostkowe', 8);
  assert.match(await dom("document.getElementById('card').innerText"), /PASS/);
  await step('Dołącz adapter CLI', 9);
  await step('Sprawdź integrację T5', 10);
  await step('Przeprowadź demonstrację', 11);
  assert.equal(await dom("document.getElementById('element').value"), 'DEMO1@1');
  await screenshot('browser-11-demo.png');
  await dom("document.querySelector('[aria-label=\"Krok 5: Przygotuj przypadki T1–T5\"]').click()");
  await wait("document.getElementById('now').textContent === 'Oglądasz krok 5 z 11'");
  assert.equal(await dom("document.querySelectorAll('#actions button').length"), 0);
  assert.equal(await dom("[...document.querySelectorAll('#element option')].some(o => o.value.startsWith('RUN'))"), false);
  const historic = await saveSession(); assert.equal(historic.cursor, 5); assert.equal(historic.commands.length, 11);
  record('PASS: historical step read-only, future results absent, cursor exported.');
  await click('Wznów sesję'); await wait("document.getElementById('load-dialog').open");
  await fill('loaded-json', JSON.stringify({...historic, lesson_version: 99}));
  await click('Odtwórz sesję'); await wait("document.getElementById('import-error').textContent.length > 0");
  assert.equal(await dom("document.getElementById('now').textContent"), 'Oglądasz krok 5 z 11');
  await click('Anuluj import'); record('PASS: invalid import did not replace state.');
  await click('Wróć do bieżącego kroku'); await wait("!document.getElementById('now').textContent.includes('Oglądasz')");
  await decision('Zgłoś korektę instrukcji','Próba techniczna: wyjaśnij rolę interpunkcji.',12);
  await decision('Popraw objaśnienie użycia','Ala,kot to jedno słowo; Ala, kot to dwa. Próba techniczna.',13);
  await step('Przeprowadź demonstrację',14);
  await decision('Odbierz I1 w fabule','W fikcyjnej lekcji rozumiem wynik i ograniczenie Q1. To test symulatora.',15);
  await wait("document.getElementById('now').textContent === 'Przyrost odebrany w fabule'");
  assert.match(await dom("document.getElementById('questions').textContent"), /Q1/);
  const saved = await saveSession(); assert.equal(saved.commands.length,15); assert.equal(saved.simulated,true);
  await writeFile(path.join(evidence, 'browser-session.json'), JSON.stringify(saved, null, 2) + '\n');
  await screenshot('browser-15-accepted.png');
  await dom("document.querySelector('[aria-label=\"Produkt: Specyfikacja wymagań\"]').focus()");
  await cdp('Input.dispatchKeyEvent',{type:'keyDown', key:'Enter', code:'Enter', windowsVirtualKeyCode:13});
  await cdp('Input.dispatchKeyEvent',{type:'keyUp', key:'Enter', code:'Enter', windowsVirtualKeyCode:13});
  await wait("document.getElementById('element').value === 'R2@1'");
  assert.match(await dom("document.getElementById('card').innerText"), /WP\.13/);
  record('PASS: graph keyboard selection opens requirement card with WP/ID/revision and reverse links.');
  await stop(server);
  const resumedURL = await startServer();
  await cdp('Page.navigate', {url: resumedURL});
  await wait("document.getElementById('now').textContent === 'Uzgodnij zakres w fabule'");
  await click('Wznów sesję'); await wait("document.getElementById('load-dialog').open");
  await fill('loaded-json', JSON.stringify(saved)); await click('Odtwórz sesję');
  await wait("document.getElementById('now').textContent === 'Przyrost odebrany w fabule'");
  assert.deepEqual(await saveSession(), saved);
  record('PASS: actual server restart and UI import/export roundtrip retained exact commands, notes, cursor.');
  const capped = {...saved, commands: saved.commands.slice(0, 11), cursor: 200};
  while (capped.commands.length < 200) {
    const action = ['reject', 'clarify', 'demo'][(capped.commands.length - 11) % 3];
    capped.commands.push({action, note: action === 'demo' ? '' : 'Próba granicy sesji.'});
  }
  await click('Wznów sesję'); await wait("document.getElementById('load-dialog').open");
  await fill('loaded-json', JSON.stringify(capped)); await click('Odtwórz sesję');
  await wait("document.querySelector('#counters .metric strong')?.textContent === '200'");
  assert.doesNotMatch(await dom("document.getElementById('actions').innerText"), /odebrany/i);
  assert.equal(await dom("[...document.querySelectorAll('#element option')].some(o => o.value.startsWith('ACC1'))"), false);
  record('PASS: reaching the session limit is not displayed as acceptance.');
  await cdp('Emulation.setDeviceMetricsOverride', {width:390, height:844, deviceScaleFactor:1, mobile:false});
  const width = await dom('({page:document.documentElement.scrollWidth, viewport:window.innerWidth})');
  assert.ok(width.page <= width.viewport, `Horizontal page overflow: ${JSON.stringify(width)}`);
  await screenshot('browser-mobile.png'); record('PASS: narrow viewport has no page-level horizontal overflow.');
  record('RESULT: PASS. Real browser checks of simulator; all TextStats outcomes remain simulated.');
} catch (error) {
  record(`RESULT: FAIL\n${error.stack}`);
  if (session) { try { await screenshot('browser-failure.png'); } catch {} }
  process.exitCode = 1;
} finally {
  socket?.close(); await stop(chrome); await stop(server);
  await rm(profile, {recursive:true, force:true});
  await writeFile(path.join(evidence, 'browser-check.log'), transcript.join('\n')+'\n');
}
