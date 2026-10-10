
const API_BASE = '/api';

async function apiCall(endpoint, method = 'GET', body = null) {
    const token = localStorage.getItem('token');
    const headers = { 'Content-Type': 'application/json' };
    if (token) headers['Authorization'] = `Bearer ${token}`;

    const config = { method, headers };
    if (body) config.body = JSON.stringify(body);

    const res = await fetch(`${API_BASE}${endpoint}`, config);
    if (res.status === 401) {
        localStorage.removeItem('token');
        window.location.href = 'login.html';
    }
    if (!res.ok) throw new Error(await res.text());
    if (res.status === 204) return null;
    return await res.json();
}
