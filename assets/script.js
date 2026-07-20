/* ===== Dark Mode Toggle ===== */
const themeToggle = document.getElementById("theme-toggle");
const html = document.documentElement;

function getPreferredTheme() {
    const stored = localStorage.getItem("theme");
    if (stored) return stored;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function setTheme(theme) {
    html.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
    if (themeToggle) {
        themeToggle.textContent = theme === "dark" ? "☀️" : "🌙";
        themeToggle.setAttribute("aria-label", theme === "dark" ? "切换到亮色模式" : "切换到暗色模式");
    }
}

if (themeToggle) {
    themeToggle.addEventListener("click", () => {
        const current = html.getAttribute("data-theme") || "light";
        setTheme(current === "dark" ? "light" : "dark");
    });
}

setTheme(getPreferredTheme());

/* ===== Tag Filtering ===== */
function filterByTag(tag) {
    const cards = document.querySelectorAll(".post-card");
    cards.forEach(card => {
        const tags = (card.dataset.tags || "").split(",").map(t => t.trim());
        if (!tag || tags.includes(tag)) {
            card.style.display = "";
        } else {
            card.style.display = "none";
        }
    });

    // Update active state on tag pills
    document.querySelectorAll(".tag-pill").forEach(pill => {
        pill.classList.toggle("active", pill.dataset.tag === tag);
    });
}

/* ===== RSS link auto-discovery ===== */
const rssLink = document.querySelector('link[type="application/rss+xml"]');
if (rssLink && !document.querySelector('link[type="application/rss+xml"][rel="alternate"]')) {
    // Already present in HTML head, no action needed
}
