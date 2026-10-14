# CLAUDE.md — vincentlauriat.github.io

## Rule: the whole site is trilingual (FR / EN / 中文 zh-Hant)

Every page of this site, with no exception (hub, project sheets, `netdisco-privacy/*`, any future page),
must be available in French, English and Traditional Chinese. Never ship FR-only or EN-only copy.

Same mechanism everywhere, so the visitor's choice carries over from page to page:

- Markup: every string exists as `<span class="en">…</span><span class="fr">…</span><span class="zh">…</span>`
  (or a `div` wrapper per language for long prose). Proper names, brands, commands and numbers stay untranslated.
- Hiding rules live in `assets/base.css` (hub) or are inlined (`netdisco-privacy/`); only hiding rules, never display rules.
- State: `<body class="lang-en|lang-fr|lang-zh">`, `<html lang>` set to `en`, `fr`, `zh-Hant`.
- Switcher: `.langs` group with `button[data-lang]` (EN / FR / 中文), driven by `assets/monograph/v1/monograph.js`
  (or `setLang()` in `index.html`).
- Storage: `localStorage` key `vl-lang`; default = saved value, else browser language (zh → zh, fr → fr, otherwise en).
- Legal pages (privacy): add a note saying the French version prevails in case of discrepancy.

Check before merging: each `en` span has its `fr` and `zh` sibling; screenshot the page in the three languages
(Chrome headless, force `localStorage['vl-lang']`), desktop and ~390 px.

## Git
Feature branch + PR, never push to `main`. Conventional commits in English.
Session-tracking files (`COMMANDS.md`, `MEMORY.md`, `CHANGES.md`, `TODOS.md`, `PLAN.md`) are git-ignored: do not force-add them.
