"""Adds breadcrumbs to every game page: wobqqq › Cat & Duck Studio › <game> › <privacy>.

Game pages are copied here from each game's `website/` folder, so the crumbs are
added by this script, not by hand: run it after every copy (idempotent).

    python3 tool/breadcrumbs.py .

Each page gets a visible <nav> at the top of <main> and a schema.org
BreadcrumbList (JSON-LD) in <head>, both between `crumbs:start/end` markers.
"""
import html
import json
import pathlib
import re
import sys

SITE = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
BASE = 'https://wobqqq.github.io/'
GAMES = ['bag-of-bags', 'zakatki', 'kto-menya-zaper', 'dacha', 'skanvordy', 'dveri-zakryvayutsya']
TEXT = {
    'ru': {'studio': BASE + 'cat-and-duck-studio/ru/', 'privacy': 'Политика конфиденциальности', 'label': 'Навигация'},
    'en': {'studio': BASE + 'cat-and-duck-studio/', 'privacy': 'Privacy policy', 'label': 'Breadcrumb'},
}
STYLE = ('<style>.crumbs{font-size:14px;line-height:1.4;margin:0 0 18px;color:var(--soft,#6b5444)}'
         '.crumbs ol{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:4px 0}'
         '.crumbs li+li::before{content:"›";margin:0 8px;opacity:.6}'
         '.crumbs a{color:inherit;text-decoration:none;border-bottom:1px solid transparent}'
         '.crumbs a:hover{color:var(--accent,#b5481a);border-bottom-color:currentColor}'
         '.crumbs [aria-current]{color:var(--ink,#3a2a1e);font-weight:600}</style>')
MARK = re.compile(r'\s*<!-- crumbs:start -->.*?<!-- crumbs:end -->', re.S)


def game_name(page: pathlib.Path) -> str:
    """The game's name is the <h1> of its home page in that language."""
    m = re.search(r'<h1>(.*?)</h1>', page.read_text(encoding='utf-8'), re.S)
    return re.sub(r'<[^>]+>', '', m.group(1)).strip() if m else page.parent.name


def crumbs(lang: str, trail: list[tuple[str, str]]) -> tuple[str, str]:
    items = []
    for i, (name, url) in enumerate(trail):
        name_h = html.escape(name)
        if i == len(trail) - 1:
            items.append(f'<li><span aria-current="page">{name_h}</span></li>')
        else:
            items.append(f'<li><a href="{url}">{name_h}</a></li>')
    nav = (f'<!-- crumbs:start -->{STYLE}<nav class="crumbs" aria-label="{TEXT[lang]["label"]}">'
           f'<ol>{"".join(items)}</ol></nav><!-- crumbs:end -->')
    data = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(trail)]}
    ld = (f'<!-- crumbs:start --><script type="application/ld+json">'
          f'{json.dumps(data, ensure_ascii=False)}</script><!-- crumbs:end -->')
    return nav, ld


def apply(page: pathlib.Path, lang: str, trail):
    src = MARK.sub('', page.read_text(encoding='utf-8'))
    nav, ld = crumbs(lang, trail)
    if '<main>' not in src or '</head>' not in src:
        print(f'skip {page}: no <main> or </head>')
        return
    src = src.replace('</head>', f'{ld}\n</head>', 1).replace('<main>', f'<main>\n{nav}', 1)
    page.write_text(src, encoding='utf-8')


count = 0
for slug in GAMES:
    for lang, folder in (('ru', SITE / slug), ('en', SITE / slug / 'en')):
        home = folder / 'index.html'
        if not home.exists():
            continue
        name = game_name(home)
        game_url = f'{BASE}{slug}/' + ('' if lang == 'ru' else 'en/')
        root = [('wobqqq', BASE), ('Cat & Duck Studio', TEXT[lang]['studio'])]
        apply(home, lang, root + [(name, game_url)])
        count += 1
        privacy = folder / 'privacy.html'
        if privacy.exists():
            apply(privacy, lang, root + [(name, game_url), (TEXT[lang]['privacy'], game_url + 'privacy.html')])
            count += 1
print(f'OK   breadcrumbs on {count} pages')
