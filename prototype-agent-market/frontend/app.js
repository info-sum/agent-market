const API = 'http://172.30.248.228:8000';

const el = {
  collections: document.getElementById('collections'),
  skills: document.getElementById('skills'),
  agents: document.getElementById('agents'),
  q: document.getElementById('q'),
  category: document.getElementById('category'),
  verified: document.getElementById('verified'),
  sort: document.getElementById('sort'),
  searchBtn: document.getElementById('searchBtn'),
};

const money = (v) => new Intl.NumberFormat('ko-KR').format(v) + '원';

async function fetchJSON(url, options) {
  const res = await fetch(url, options);
  if (!res.ok) throw new Error('API Error');
  return await res.json();
}

function renderCollections(items) {
  el.collections.innerHTML = `
    <h2>Collections</h2>
    <div class="grid">
      ${items
        .map(
          (c) => `
        <div class="card">
          <div class="small">${c.id}</div>
          <h3>${c.name}</h3>
          <div>Floor: <b>${money(c.floor_price)}</b></div>
          <div class="small">7d Volume: ${money(c.volume_7d)}</div>
        </div>`
        )
        .join('')}
    </div>`;
}

function renderAgents(items) {
  el.agents.innerHTML = items
    .map(
      (a) => `
    <div class="card">
      <div style="font-size: 24px">${a.avatar}</div>
      <h3>${a.name}</h3>
      <div class="small">${a.specialty}</div>
      <div class="small">Followers: ${a.followers}</div>
    </div>`
    )
    .join('');
}

function skillCard(s) {
  return `
    <div class="card">
      <div class="small">${s.id}</div>
      <h3>${s.name}</h3>
      <div>
        <span class="badge">${s.category}</span>
        <span class="badge">${s.verified}</span>
      </div>
      <p class="small">${s.description}</p>
      <div class="small">Owner: ${s.owner_agent}</div>
      <div class="small">OpenClaw: ${s.openclaw_version}</div>
      <div class="small">⭐ ${s.rating} / installs ${s.installs}</div>
      <div class="price">${money(s.price)}</div>
      <button data-buy="${s.id}">구매(프로토타입)</button>
    </div>`;
}

function bindBuyButtons() {
  document.querySelectorAll('[data-buy]').forEach((btn) => {
    btn.addEventListener('click', async () => {
      const id = btn.getAttribute('data-buy');
      try {
        const result = await fetchJSON(`${API}/api/skills/${id}/purchase`, { method: 'POST' });
        alert(result.message);
        loadSkills();
      } catch {
        alert('구매 실패');
      }
    });
  });
}

async function loadSkills() {
  const params = new URLSearchParams({
    q: el.q.value,
    category: el.category.value,
    verified: el.verified.value,
    sort: el.sort.value,
  });
  Object.keys(Object.fromEntries(params)).forEach((k) => !params.get(k) && params.delete(k));

  const skills = await fetchJSON(`${API}/api/skills?${params.toString()}`);
  el.skills.innerHTML = skills.map(skillCard).join('');
  bindBuyButtons();
}

async function init() {
  const [collections, agents] = await Promise.all([
    fetchJSON(`${API}/api/collections`),
    fetchJSON(`${API}/api/agents`),
  ]);
  renderCollections(collections);
  renderAgents(agents);
  await loadSkills();
}

el.searchBtn.addEventListener('click', loadSkills);
init().catch(() => alert('백엔드 연결 실패: backend 실행 상태를 확인하세요.'));
