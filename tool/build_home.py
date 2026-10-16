"""Builds the wobqqq.github.io home page (EN at /, RU at /ru/) into the given folder.

The studio lives in its own repo (https://wobqqq.github.io/cat-and-duck-studio/);
game pages and privacy policies stay here, one folder per game.
"""
import json
import pathlib
import sys

SITE = pathlib.Path(sys.argv[1])
GH = 'https://github.com/wobqqq/'
STUDIO = 'https://wobqqq.github.io/cat-and-duck-studio/'
GAMES = ['bag-of-bags', 'zakatki', 'kto-menya-zaper', 'dacha', 'skanvordy']

MONO = '''<svg class="mono" viewBox="0 0 64 64" aria-hidden="true">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6d5dfc"/><stop offset="1" stop-color="#22b8cf"/></linearGradient></defs>
  <rect width="64" height="64" rx="18" fill="url(#g)"/>
  <path d="M14 22 l7 22 l7 -16 l4 9 l4 -9 l7 16 l7 -22" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

DUCK = '''<svg class="studio-logo" viewBox="0 0 120 120" aria-hidden="true">
  <circle cx="60" cy="60" r="58" fill="#fff1da"/>
  <path d="M30 60 L28 30 L50 46 Z" fill="#f2994a"/><path d="M90 60 L92 30 L70 46 Z" fill="#f2994a"/>
  <path d="M33 54 L32 37 L45 47 Z" fill="#ffc9a8"/><path d="M87 54 L88 37 L75 47 Z" fill="#ffc9a8"/>
  <ellipse cx="60" cy="72" rx="35" ry="28" fill="#f2994a"/>
  <path d="M44 66 q4 -5 8 0" stroke="#3a2a1e" stroke-width="3.2" fill="none" stroke-linecap="round"/>
  <path d="M68 66 q4 -5 8 0" stroke="#3a2a1e" stroke-width="3.2" fill="none" stroke-linecap="round"/>
  <path d="M57 74 h6 l-3 3.5 z" fill="#c2553a"/>
  <path d="M60 77.5 q-4 5 -8 2 M60 77.5 q4 5 8 2" stroke="#3a2a1e" stroke-width="2.4" fill="none" stroke-linecap="round"/>
  <circle cx="41" cy="77" r="4.5" fill="#ff8f7a" opacity=".55"/><circle cx="79" cy="77" r="4.5" fill="#ff8f7a" opacity=".55"/>
  <g transform="translate(60 26) rotate(-6)">
    <ellipse cx="0" cy="10" rx="17" ry="11" fill="#ffd25a"/><circle cx="-4" cy="-4" r="10" fill="#ffd25a"/>
    <path d="M-14 -4 q-9 1 -10 4 q6 2 11 0 z" fill="#f28c28"/><circle cx="-6" cy="-6" r="2" fill="#3a2a1e"/>
    <path d="M6 6 q8 -6 12 2 q-6 4 -12 2 z" fill="#f5bf2e"/>
  </g>
</svg>'''

# (emoji, title, text{en,ru}, tags, links[(label, url)])
PROJECTS = [
    ('🛡️', 'Aegis', {
        'en': 'Security suite for Laravel Nova: hardening checks, scanners and a dashboard card, plus five add-on modules.',
        'ru': 'Набор безопасности для Laravel Nova: проверки, сканеры и карточка на дашборде, плюс пять модулей.'},
     ['PHP', 'Laravel', 'Nova'],
     [('nova-aegis', GH + 'nova-aegis'), ('IP access', GH + 'nova-aegis-admin-ip-access'),
      ('IP blocker', GH + 'nova-aegis-ip-blocker'), ('Smart blocker', GH + 'nova-aegis-smart-ip-blocker'),
      ('CSP', GH + 'nova-aegis-csp'), ('Sanitizer', GH + 'nova-aegis-input-sanitizer')]),
    ('🏰', 'Fortify', {
        'en': 'The same security suite for October CMS: diagnostics, hardening and the same five modules.',
        'ru': 'Тот же набор безопасности для October CMS: диагностика, защита и те же пять модулей.'},
     ['PHP', 'October CMS'],
     [('fortify', GH + 'oc-fortify-plugin'), ('IP access', GH + 'oc-fortify-admin-ip-access-plugin'),
      ('IP blocker', GH + 'oc-fortify-ip-blocker-plugin'), ('Smart blocker', GH + 'oc-fortify-smart-ip-blocker-plugin'),
      ('CSP', GH + 'oc-fortify-csp-plugin'), ('Sanitizer', GH + 'oc-fortify-input-sanitizer-plugin')]),
    ('🗺️', 'sitemap-audit', {
        'en': 'Cross-platform sitemap auditor: checks every URL (status, redirects, noindex, canonical, hreflang) and writes HTML, Excel, JSON and CSV reports.',
        'ru': 'Кроссплатформенный аудит sitemap: проверяет каждый URL (статус, редиректы, noindex, canonical, hreflang) и пишет отчёты HTML, Excel, JSON и CSV.'},
     ['Go', 'CLI', 'SEO'], [('GitHub', GH + 'sitemap-audit')]),
    ('🧠', 'oc-ide-helper', {
        'en': 'IDE and PHPStan-ready docblocks for October CMS models.',
        'ru': 'Докблоки для IDE и PHPStan у моделей October CMS.'},
     ['PHP', 'PHPStan'], [('GitHub', GH + 'oc-ide-helper')]),
    ('🧪', 'Sandboxes', {
        'en': 'Clean Laravel Nova and October CMS apps in Docker for developing and testing packages locally.',
        'ru': 'Чистые приложения Laravel Nova и October CMS в Docker для разработки и проверки пакетов.'},
     ['Docker', 'Pest', 'PHPStan'],
     [('Nova sandbox', GH + 'laravel-nova-sandbox'), ('October sandbox', GH + 'october-cms-sandbox')]),
    ('🐧', 'Linux', {
        'en': 'PredatorSense for Linux (fans, thermal profiles, RGB keyboard) and post-install scripts for Fedora Workstation.',
        'ru': 'PredatorSense для Linux (вентиляторы, профили, RGB-клавиатура) и скрипты настройки Fedora Workstation.'},
     ['Bash', 'DKMS', 'Fedora'],
     [('predator-sense', GH + 'predator-sense'), ('fedora-apps', GH + 'fedora-apps')]),
]

T = {
    'en': {
        'title': 'Sergey Zakharevich (wobqqq) — backend developer and Cat & Duck Studio',
        'desc': 'Senior backend developer and software architect: open-source security tools for Laravel Nova and October CMS, and cozy mobile games by Cat & Duck Studio.',
        'hi': 'Hi, I’m Sergey', 'role': 'Senior Backend Developer & Software Architect',
        'lead': 'I build secure, high-load backends with PHP, Laravel and Node.js, integrate AI — and in my spare time make cozy mobile games.',
        'where': 'Minsk, Belarus',
        'studio_kicker': 'My game studio', 'studio_text': 'Cozy mobile games: puzzles, words and a country garden. Offline, no sign-up.',
        'studio_btn': 'Visit the studio', 'games': 'games on Android',
        'oss': 'Open source', 'oss_lead': 'Libraries and tools I build and maintain on GitHub.',
        'contact': 'Get in touch',
    },
    'ru': {
        'title': 'Сергей Захаревич (wobqqq) — backend-разработчик и Cat & Duck Studio',
        'desc': 'Senior backend-разработчик и архитектор: открытые инструменты безопасности для Laravel Nova и October CMS и уютные мобильные игры Cat & Duck Studio.',
        'hi': 'Привет, я Сергей', 'role': 'Senior Backend Developer и архитектор ПО',
        'lead': 'Делаю надёжные и нагруженные бэкенды на PHP, Laravel и Node.js, встраиваю ИИ — а в свободное время делаю уютные мобильные игры.',
        'where': 'Минск, Беларусь',
        'studio_kicker': 'Моя игровая студия', 'studio_text': 'Уютные мобильные игры: головоломки, слова и дача. Без интернета и регистрации.',
        'studio_btn': 'Открыть студию', 'games': 'игр на Android',
        'oss': 'Открытый код', 'oss_lead': 'Библиотеки и инструменты, которые я делаю и поддерживаю на GitHub.',
        'contact': 'Связаться',
    },
}

CSS = '''
:root { --bg: #f7f7fb; --card: #ffffff; --ink: #1c1b29; --soft: #5d5b72; --line: #e6e5ef; --chip: #efeefa;
  --a1: #6d5dfc; --a2: #22b8cf; --shadow: 0 1px 0 var(--line), 0 12px 30px rgba(40, 30, 120, .07); }
@media (prefers-color-scheme: dark) {
  :root { --bg: #111019; --card: #1b1a27; --ink: #f1f0fa; --soft: #a9a7c0; --line: #2a2939; --chip: #252436;
    --shadow: 0 1px 0 #0a0910, 0 12px 30px rgba(0, 0, 0, .35); }
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink); font: 17px/1.6 "Inter", system-ui, sans-serif; }
a { color: var(--a1); }
.wrap { max-width: 1080px; margin: 0 auto; padding: 0 16px; }
.top { display: flex; justify-content: space-between; align-items: center; padding: 18px 0; }
.brand { display: flex; align-items: center; gap: 10px; font-weight: 800; color: var(--ink); text-decoration: none; }
.brand .mono { width: 34px; height: 34px; }
.switch { display: flex; gap: 2px; background: var(--chip); padding: 4px; border-radius: 999px; }
.switch a { color: var(--soft); text-decoration: none; font-weight: 700; font-size: 14px; padding: 5px 12px; border-radius: 999px; }
.switch a[aria-current="page"] { background: var(--card); color: var(--ink); box-shadow: 0 1px 0 var(--line); }
.hero { padding: 56px 0 40px; display: grid; grid-template-columns: 1fr auto; gap: 32px; align-items: center; }
.hero .hi { font-weight: 700; color: var(--soft); margin: 0 0 8px; }
.hero h1 { font-size: clamp(34px, 6vw, 60px); line-height: 1.05; margin: 0 0 14px; letter-spacing: -.03em; font-weight: 800;
  background: linear-gradient(90deg, var(--a1), var(--a2)); -webkit-background-clip: text; background-clip: text; color: transparent; }
.hero p.lead { max-width: 620px; margin: 0 0 22px; color: var(--soft); font-size: 18px; }
.hero .mono { width: clamp(110px, 18vw, 180px); height: auto; filter: drop-shadow(0 16px 26px rgba(109, 93, 252, .35)); transform: rotate(-6deg); }
.links { display: flex; flex-wrap: wrap; gap: 10px; }
.btn { display: inline-flex; align-items: center; gap: 8px; padding: 10px 16px; border-radius: 14px; background: var(--card); color: var(--ink); text-decoration: none; font-weight: 700; font-size: 15px; box-shadow: var(--shadow); }
.btn.primary { background: linear-gradient(90deg, var(--a1), var(--a2)); color: #fff; }
.btn svg { width: 18px; height: 18px; fill: currentColor; }
.where { color: var(--soft); font-size: 15px; margin-top: 14px; }
.studio { display: grid; grid-template-columns: auto 1fr auto; gap: 24px; align-items: center; padding: 26px; border-radius: 28px; margin: 12px 0 52px; text-decoration: none; color: #2d241c;
  background: radial-gradient(circle at 90% 10%, rgba(255, 210, 90, .7), transparent 45%), linear-gradient(120deg, #ffe7c2, #ffd9a8); box-shadow: 0 18px 40px rgba(242, 153, 74, .25); transition: transform .18s; }
.studio:hover { transform: translateY(-3px); }
.studio .studio-logo { width: 110px; height: 110px; }
.studio .kicker { margin: 0; font-size: 13px; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; color: #b5481a; }
.studio h2 { margin: 2px 0 6px; font-size: clamp(26px, 4vw, 36px); line-height: 1.1; font-weight: 800; }
.studio p { margin: 0 0 12px; color: #6b5444; }
.studio .icons { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
.studio .icons img { width: 40px; height: 40px; border-radius: 11px; box-shadow: 0 3px 8px rgba(90, 55, 20, .2); }
.studio .icons span { font-size: 14px; font-weight: 700; color: #6b5444; margin-left: 4px; }
.studio .go { background: #b5481a; color: #fff; padding: 12px 18px; border-radius: 16px; font-weight: 800; white-space: nowrap; }
h2.sec { font-size: 30px; margin: 0 0 4px; letter-spacing: -.02em; }
p.sec { color: var(--soft); margin: 0 0 20px; }
.grid { list-style: none; padding: 0; margin: 0; display: grid; gap: 16px; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); }
.card { background: var(--card); border-radius: 22px; padding: 20px; box-shadow: var(--shadow); display: flex; flex-direction: column; gap: 10px; }
.card h3 { margin: 0; font-size: 20px; display: flex; align-items: center; gap: 10px; }
.card h3 i { font-style: normal; font-size: 24px; }
.card p { margin: 0; color: var(--soft); font-size: 15px; flex: 1; }
.tags { display: flex; gap: 6px; flex-wrap: wrap; }
.tag { font-size: 12px; font-weight: 700; padding: 2px 9px; border-radius: 999px; background: var(--chip); color: var(--soft); }
.repo { display: flex; gap: 6px; flex-wrap: wrap; }
.repo a { font-size: 13px; font-weight: 700; text-decoration: none; padding: 5px 10px; border-radius: 10px; border: 1px solid var(--line); color: var(--ink); }
.repo a:hover { border-color: var(--a1); color: var(--a1); }
footer { margin-top: 56px; padding: 28px 0 48px; border-top: 1px solid var(--line); display: flex; justify-content: space-between; gap: 16px; flex-wrap: wrap; color: var(--soft); font-size: 15px; }
@media (max-width: 760px) {
  .hero { grid-template-columns: 1fr; padding-top: 28px; }
  .hero .mono { order: -1; width: 88px; }
  .studio { grid-template-columns: 1fr; text-align: left; }
  .studio .studio-logo { width: 84px; height: 84px; }
  .studio .go { justify-self: start; }
  .grid { grid-template-columns: 1fr; }
}
'''

ICON = {
    'github': '<svg viewBox="0 0 24 24"><path d="M12 .5a12 12 0 0 0-3.8 23.4c.6.1.8-.3.8-.6v-2c-3.3.7-4-1.6-4-1.6-.6-1.4-1.4-1.8-1.4-1.8-1.1-.7.1-.7.1-.7 1.2.1 1.9 1.3 1.9 1.3 1.1 1.8 2.9 1.3 3.6 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.5.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0C17.3 4.7 18.3 5 18.3 5c.7 1.7.3 2.9.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0 0 12 .5z"/></svg>',
    'linkedin': '<svg viewBox="0 0 24 24"><path d="M20.4 20.5h-3.6v-5.6c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9v5.7H9.3V9h3.4v1.6h.1c.5-.9 1.6-1.8 3.4-1.8 3.6 0 4.3 2.4 4.3 5.5v6.2zM5.3 7.4a2.1 2.1 0 1 1 0-4.2 2.1 2.1 0 0 1 0 4.2zM7.1 20.5H3.5V9h3.6v11.5zM22.2 0H1.8C.8 0 0 .8 0 1.7v20.6c0 .9.8 1.7 1.8 1.7h20.4c1 0 1.8-.8 1.8-1.7V1.7C24 .8 23.2 0 22.2 0z"/></svg>',
    'telegram': '<svg viewBox="0 0 24 24"><path d="M23.6 3.3 20 20.4c-.3 1.2-1 1.5-2 .9l-5.5-4-2.6 2.5c-.3.3-.5.5-1.1.5l.4-5.6L19.4 5.5c.4-.4-.1-.6-.7-.2L6.1 12.4.7 10.7c-1.2-.4-1.2-1.2.2-1.7L22.2.6c1-.4 1.9.2 1.4 2.7z"/></svg>',
}


def page(lang):
    t = T[lang]
    up = '' if lang == 'en' else '../'
    studio = STUDIO if lang == 'en' else STUDIO + 'ru/'
    en_href, ru_href = ('./', 'ru/') if lang == 'en' else ('../', './')
    cur = ' aria-current="page"'
    switch = (f'<nav class="switch" aria-label="Language"><a href="{en_href}" hreflang="en"{cur if lang == "en" else ""}>EN</a>'
              f'<a href="{ru_href}" hreflang="ru"{cur if lang == "ru" else ""}>RU</a></nav>')
    icons = ''.join(f'<img src="{up}{g}/icon_512.png" alt="" width="40" height="40">' for g in GAMES)
    cards = []
    for emoji, title, text, tags, links in PROJECTS:
        tg = ''.join(f'<span class="tag">{x}</span>' for x in tags)
        ln = ''.join(f'<a href="{u}">{n}</a>' for n, u in links)
        cards.append(f'<li class="card"><h3><i>{emoji}</i>{title}</h3><div class="tags">{tg}</div><p>{text[lang]}</p><div class="repo">{ln}</div></li>')
    contacts = (f'<a class="btn primary" href="https://github.com/wobqqq">{ICON["github"]}GitHub</a>'
                f'<a class="btn" href="https://www.linkedin.com/in/wobqqq">{ICON["linkedin"]}LinkedIn</a>'
                f'<a class="btn" href="https://t.me/wobqqq">{ICON["telegram"]}Telegram</a>')
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<link rel="icon" href="{up}favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="{up}favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="{up}favicon-16.png">
<link rel="apple-touch-icon" sizes="180x180" href="{up}apple-touch-icon.png">
<link rel="manifest" href="{up}site.webmanifest">
<meta name="theme-color" content="#6d5dfc">
<meta property="og:title" content="Sergey Zakharevich (wobqqq)">
<meta property="og:description" content="{t['desc']}">
<meta property="og:image" content="https://wobqqq.github.io/icon-512.png">
<link rel="alternate" hreflang="en" href="https://wobqqq.github.io/"><link rel="alternate" hreflang="ru" href="https://wobqqq.github.io/ru/"><link rel="alternate" hreflang="x-default" href="https://wobqqq.github.io/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header class="top"><a class="brand" href="./">{MONO}<span>wobqqq</span></a>{switch}</header>
<section class="hero">
  <div>
    <p class="hi">{t['hi']} 👋</p>
    <h1>{t['role']}</h1>
    <p class="lead">{t['lead']}</p>
    <div class="links">{contacts}</div>
    <p class="where">📍 {t['where']}</p>
  </div>
  {MONO}
</section>
<a class="studio" href="{studio}">
  {DUCK}
  <div><p class="kicker">{t['studio_kicker']}</p><h2>Cat &amp; Duck Studio</h2><p>{t['studio_text']}</p><div class="icons">{icons}<span>{len(GAMES)} {t['games']}</span></div></div>
  <span class="go">{t['studio_btn']} →</span>
</a>
<h2 class="sec">{t['oss']}</h2>
<p class="sec">{t['oss_lead']}</p>
<ul class="grid">
{chr(10).join(cards)}
</ul>
<footer><span>© 2026 Sergey Zakharevich</span><span>{t['contact']}: <a href="https://t.me/wobqqq">Telegram</a> · <a href="https://www.linkedin.com/in/wobqqq">LinkedIn</a> · <a href="https://github.com/wobqqq">GitHub</a></span></footer>
</div>
</body>
</html>
'''


(SITE / 'index.html').write_text(page('en'))
(SITE / 'ru').mkdir(exist_ok=True)
(SITE / 'ru' / 'index.html').write_text(page('ru'))
(SITE / 'tool' / 'logo.svg').write_text(
    MONO.replace('class="mono" ', 'xmlns="http://www.w3.org/2000/svg" width="512" height="512" ').replace(' aria-hidden="true"', ''))
(SITE / 'site.webmanifest').write_text(json.dumps({
    'name': 'wobqqq', 'short_name': 'wobqqq', 'start_url': './', 'scope': './', 'display': 'browser',
    'background_color': '#f7f7fb', 'theme_color': '#6d5dfc',
    'icons': [{'src': 'icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
              {'src': 'icon-512.png', 'sizes': '512x512', 'type': 'image/png'}],
}, indent=1))
