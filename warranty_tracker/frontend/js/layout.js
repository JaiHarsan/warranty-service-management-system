
function renderNav() {
    const nav = document.createElement('nav');
    nav.innerHTML = `
        <div class="nav-container">
            <a href="dashboard.html" class="brand">WarrantyCare</a>
            <div class="nav-links">
                <a href="dashboard.html">Dashboard</a>
                <a href="products.html">My Products</a>
                <a href="service-centres.html">Service Centres</a>
                <button onclick="logout()">Logout</button>
            </div>
        </div>
    `;
    document.body.prepend(nav);
}

function logout() {
    apiCall('/logout/', 'POST').then(() => {
        localStorage.removeItem('token');
        window.location.href = 'login.html';
    });
}
document.addEventListener('DOMContentLoaded', () => {
    if(!window.location.href.includes('login.html')) renderNav();
});
