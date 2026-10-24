const $ = id => document.getElementById(id);
let view, selected, pendingAction, busy = false;
const svgNS = 'http://www.w3.org/2000/svg';

function element(tag, text, className) {
  const node = document.createElement(tag);
  if (text !== undefined) node.textContent = text;
  if (className) node.className = className;
  return node;
}
function svgElement(tag, attrs = {}, text) {
  const node = document.createElementNS(svgNS, tag);
  for (const [key, value] of Object.entries(attrs)) node.setAttribute(key, value);
  if (text !== undefined) node.textContent = text;
  return node;
}
async function api(path, payload) {
  const response = await fetch(path, payload === undefined ? {} : {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: typeof payload === 'string' ? payload : JSON.stringify(payload)
  });
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || `Błąd HTTP ${response.status}`);
  return data;
}
function announce(text) { $('message').textContent = text; }
async function change(path, payload) {
  if (busy) return;
  busy = true;
  try {
    view = await api(path, {...payload, version: view.version});
    if (path === '/api/command') selected = view.history.at(-1)?.outputs.at(-1);
    render(); announce('');
  } catch (error) { announce(error.message); }
  finally { busy = false; }
}
function choose(key) {
  selected = key;
  renderCard(); renderGraph();
}
function renderActions() {
  $('actions').replaceChildren(); $('other-actions').replaceChildren();
  for (const action of view.actions) {
    const block = element('div', undefined, 'action');
    block.append(element('div', `${action.done ? '✓ ' : ''}${action.phase}`, 'phase'));
    const button = element('button', action.title, action.enabled ? 'primary' : '');
    button.disabled = !action.enabled;
    button.addEventListener('click', () => {
      if (busy) return;
      if (action.needs_note) {
        pendingAction = action.id;
        $('action-title').textContent = action.title;
        $('action-help').textContent = action.reason;
        $('note').value = '';
        $('action-dialog').showModal();
        $('note').focus();
      } else change('/api/command', {action: action.id, note: ''});
    });
    block.append(button, element('small', `${action.actor}. ${action.reason}`));
    $(action.enabled ? 'actions' : 'other-actions').append(block);
  }
  if (!view.actions.some(a => a.enabled)) {
    $('actions').append(element('p', view.read_only ? 'Historia: tylko odczyt.' : view.accepted ? 'I1 odebrany w fabule. Q1 nadal blokuje wydanie.' : 'Brak dostępnych działań. Sprawdź warunki poniżej.', 'muted'));
  }
}
function renderGraph() {
  const positions = new Map(), rows = [0, 0, 0, 0, 0];
  const selectedCard = view.cards.find(c => c.key === selected);
  for (const node of view.nodes) {
    positions.set(node.id, {x: 8 + node.column * 145, y: 32 + rows[node.column]++ * 91});
  }
  const height = Math.max(...rows, 3) * 91 + 42;
  const svg = svgElement('svg', {viewBox: `0 0 733 ${height}`, role: 'group', 'aria-label': 'Graf produktów pracy'});
  const defs = svgElement('defs');
  const marker = svgElement('marker', {id: 'arrow', viewBox: '0 0 10 10', refX: 9, refY: 5, markerWidth: 5, markerHeight: 5, orient: 'auto-start-reverse'});
  marker.append(svgElement('path', {d: 'M 0 0 L 10 5 L 0 10 z', fill: '#8ca995'}));
  defs.append(marker); svg.append(defs);
  ['KONTEKST', 'CEL I PLAN', 'PRZYGOTOWANIE', 'KOD I WYNIKI', 'OCENA'].forEach((label, i) => {
    svg.append(svgElement('text', {x: 8 + i * 145, y: 15, class: 'column-title'}, label));
  });
  for (const [from, to] of view.edges) {
    const a = positions.get(from), b = positions.get(to);
    const sameColumn = a.x === b.x;
    const x1 = sameColumn ? a.x + 64 : a.x + 130;
    const y1 = sameColumn ? a.y + 65 : a.y + 32;
    const x2 = sameColumn ? b.x + 64 : b.x;
    const y2 = sameColumn ? b.y : b.y + 32;
    const mid = (x1 + x2) / 2;
    const path = sameColumn ? `M${x1},${y1} L${x2},${y2}` : `M${x1},${y1} C${mid},${y1} ${mid},${y2} ${x2},${y2}`;
    svg.append(svgElement('path', {d: path, class: `edge ${selectedCard && [from,to].includes(selectedCard.path) ? 'highlight' : ''}`, 'marker-end': 'url(#arrow)'}));
  }
  for (const node of view.nodes) {
    const {x, y} = positions.get(node.id);
    const group = svgElement('g', {class: `node ${selectedCard?.path === node.id ? 'selected' : ''}`, tabindex: '0', role: 'button', 'aria-label': `Produkt: ${node.title}`, transform: `translate(${x} ${y})`});
    group.append(svgElement('title', {}, `${node.title}\n${node.id}\n${node.cards.join(', ')}`));
    group.append(svgElement('rect', {width: 130, height: 65, rx: 6}));
    group.append(svgElement('text', {x: 9, y: 16, class: 'meta'}, node.wp === '—' ? 'LOKALNY ZAPIS' : node.wp));
    const label = node.title.split(' — ')[0].replace(' (fragment WP.10)', '').replace(' (adaptacja)', '');
    const words = label.split(' '); let line = '', lines = [];
    for (const word of words) {
      if ((line + ' ' + word).trim().length > 20 && line) { lines.push(line); line = word; }
      else line = (line + ' ' + word).trim();
    }
    if (line) lines.push(line);
    lines.slice(0, 2).forEach((line, i) => group.append(svgElement('text', {x: 9, y: 32 + i * 13}, line)));
    group.append(svgElement('text', {x: 9, y: 58, class: 'meta'}, `${node.cards.length} ${node.cards.length === 1 ? 'element / rewizja' : 'elementów / rewizji'}`));
    const select = () => choose(node.cards.at(-1));
    group.addEventListener('click', select);
    group.addEventListener('keydown', event => { if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); select(); } });
    svg.append(group);
  }
  $('graph').replaceChildren(svg);
  $('graph-count').textContent = `${view.nodes.length} nośników informacji · ${view.edges.length} powiązań między nimi. Szczegółowe ID i rewizje: karta po prawej.`;
}
function renderCard() {
  if (!view.cards.some(c => c.key === selected)) selected = view.cards.at(-1)?.key;
  const card = view.cards.find(c => c.key === selected);
  $('element').replaceChildren(...view.cards.map(c => {
    const option = element('option', `${c.key} · ${c.title}${c.current ? '' : ' (poprzednia rewizja)'}`);
    option.value = c.key; return option;
  }));
  $('element').value = selected;
  const contents = $('card'); contents.replaceChildren();
  if (!card) return;
  contents.append(element('h3', card.title));
  contents.append(element('span', `${card.id} · rewizja ${card.revision}`, 'badge'));
  contents.append(element('span', 'SYMULACJA', 'badge'));
  if (card.outcome) contents.append(element('span', card.outcome, `badge ${card.outcome.toLowerCase()}`));
  if (!card.current) contents.append(element('span', 'Poprzednia rewizja', 'badge'));
  contents.append(element('p', `${card.wp === '—' ? 'Lokalny zapis' : `Typ produktu: ${card.wp} (wycinek)`}\nProdukt: ${card.container}\nPrzykładowy plik: ${card.path}`, 'metadata'));
  contents.append(element('p', card.body, 'content'));
  const why = element('section', undefined, 'card-section');
  why.append(element('h4', 'Po co powstało?'), element('p', card.why)); contents.append(why);
  for (const [label, links] of [['Opiera się na', card.links], ['Jest podstawą dla', card.used_by]]) {
    const section = element('section', undefined, 'card-section'); section.append(element('h4', label));
    for (const link of links) {
      const button = element('button', link.key, 'link-button'); button.title = link.title;
      button.addEventListener('click', () => choose(link.key)); section.append(button);
    }
    if (!links.length) section.append(element('p', 'Brak powiązań w tym momencie.', 'muted'));
    contents.append(section);
  }
  contents.append(element('p', 'WP określa typ informacji, ID wskazuje element lekcji, @ wskazuje jego rewizję. Powiązanie samo w sobie nie potwierdza poprawności.', 'muted'));
}
function renderHistory() {
  $('history').replaceChildren();
  for (const item of [{step: 0, title: 'Potrzeba redaktora'}, ...view.history]) {
    const button = element('button', undefined, view.cursor === item.step ? 'active' : '');
    button.setAttribute('aria-label', `Krok ${item.step}: ${item.title}`);
    button.setAttribute('aria-current', view.cursor === item.step ? 'step' : 'false');
    button.append(element('span', `${String(item.step).padStart(2, '0')} / SYMULACJA`), element('strong', item.title));
    button.addEventListener('click', () => change('/api/cursor', {cursor: item.step}));
    $('history').append(button);
  }
  $('current').disabled = !view.read_only;
  const event = view.history[view.cursor - 1];
  $('event-detail').textContent = event ? `Powstało / zmieniono: ${event.outputs.join(', ')}. ${event.note || ''}` : 'Na początku istnieje potrzeba. Plan, kod i dowody jeszcze nie powstały.';
}
function render() {
  renderCard(); renderActions(); renderGraph(); renderHistory();
  const next = view.actions.find(a => a.enabled);
  $('now').textContent = view.read_only ? `Oglądasz krok ${view.cursor} z ${view.total}` : view.accepted ? 'Przyrost odebrany w fabule' : next?.title || 'Brak dostępnych działań';
  $('hint').textContent = view.read_only ? 'Tylko odczyt. Bieżący stan zachowano na końcu historii.' : view.accepted ? 'Odbiór I1 nie zamyka Q1 i nie jest zgodą na wydanie.' : next?.reason || view.actions[0]?.reason || '';
  $('counters').replaceChildren();
  for (const [count, label] of [[view.cursor, 'krok historii'], [new Set(view.cards.map(c => c.id)).size, 'elementów'], [view.cards.filter(c => c.kind === 'run').length, 'wykonań']]) {
    const metric = element('div', undefined, 'metric'); metric.append(element('strong', String(count)), element('span', label)); $('counters').append(metric);
  }
  $('questions').textContent = view.open_questions.join(' ') || 'Najpierw uzgodnij zakres w fabule.';
}
$('element').addEventListener('change', event => choose(event.target.value));
$('current').addEventListener('click', () => change('/api/cursor', {cursor: view.total}));
$('refresh').addEventListener('click', async () => { try { view = await api('/api/state'); render(); announce('Stan odświeżony.'); } catch (error) { announce(error.message); } });
$('action-form').addEventListener('submit', async event => {
  event.preventDefault();
  if (!$('note').value.trim()) { $('note').setCustomValidity('Podaj konkretny opis.'); $('note').reportValidity(); return; }
  $('action-dialog').close(); await change('/api/command', {action: pendingAction, note: $('note').value.trim()});
});
$('note').addEventListener('input', () => $('note').setCustomValidity(''));
$('cancel-action').addEventListener('click', () => $('action-dialog').close());
$('export').addEventListener('click', async () => {
  try { $('saved-json').value = JSON.stringify(await api('/api/export'), null, 2); $('save-dialog').showModal(); }
  catch (error) { announce(error.message); }
});
$('close-save').addEventListener('click', () => $('save-dialog').close());
$('download').addEventListener('click', () => {
  const url = URL.createObjectURL(new Blob([$('saved-json').value], {type: 'application/json'}));
  const anchor = element('a'); anchor.href = url; anchor.download = 'textstats-i1-session.json'; anchor.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
});
$('import').addEventListener('click', () => { $('import-error').textContent = ''; $('load-dialog').showModal(); });
$('cancel-load').addEventListener('click', () => $('load-dialog').close());
$('session-file').addEventListener('change', async event => {
  const file = event.target.files[0]; if (!file) return;
  if (file.size > 2000000) { $('import-error').textContent = 'Plik jest zbyt duży (limit 2 MB).'; return; }
  $('loaded-json').value = await file.text();
});
$('load-form').addEventListener('submit', async event => {
  event.preventDefault(); if (busy) return; busy = true;
  try {
    // Keep raw JSON for server-side duplicate-field and constant validation.
    view = await api('/api/import', `{"version":${view.version},"session":${$('loaded-json').value}}`);
    selected = undefined; render(); $('load-dialog').close(); announce('Sesja odtworzona przez reguły silnika.');
  } catch (error) { $('import-error').textContent = error.message; }
  finally { busy = false; }
});
try { view = await api('/api/state'); render(); } catch (error) { announce(`Nie można odczytać lekcji: ${error.message}`); }
