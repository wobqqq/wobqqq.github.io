# AGENTS.md — wobqqq.github.io

Public GitHub Pages site (served from `main`; Actions stay on because Pages needs them).

## What is here

| Path | What | Notes |
|---|---|---|
| `index.html` | owner's personal home page, English only | **generated**: edit `tool/build_home.py`, run `python3 tool/build_home.py .` |
| `tool/logo.svg`, favicons, `site.webmanifest` | home page logo and icons | written by the build script; favicons resized from the logo with Pillow |
| `<slug>/` (`bag-of-bags`, `zakatki`, `kto-menya-zaper`, `dacha`, `skanvordy`) | each game's page + privacy policy: RU at `/<slug>/`, EN at `/<slug>/en/` | **URLs are in the stores: never move or rename them**; the source is `website/` in the game's repo, copied here |

The Cat & Duck Studio catalogue is a separate repo and site: `../cat-and-duck-studio` → https://wobqqq.github.io/cat-and-duck-studio/

## How to change

- **A game page:** use the `game-site` skill in the game's repo. It edits `website/` there and copies it here. After every copy, run `python3 tool/breadcrumbs.py .`: it adds the breadcrumbs (wobqqq › Cat & Duck Studio › game › privacy) and their JSON-LD to all game pages, and running it again does no harm.
- **The home page:** edit `tool/build_home.py` (the `GAMES`, `PROJECTS` and `T` texts), rebuild, then check it at desktop and phone width.
- **Publish:** branch → commit → `gh pr create --fill` → `gh pr merge --merge --delete-branch`. After about a minute, check with `curl -s -o /dev/null -w "%{http_code}" https://wobqqq.github.io/<path>`.
- **Commits** as `Sergey Zakharevich <wobqqq@gmail.com>`, with no Co-Authored-By or "Generated with" lines.
- **Language:** code and comments in English; only the visible texts of the game pages are RU/EN.
