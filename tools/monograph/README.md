# Monograph sheet — landing page generator

Every project landing page under `vincentlauriat.github.io/<Project>/` is a *sheet* of the
monograph published by the hub: cool paper, ink, Schibsted Grotesk, one per-project accent.
Style and behaviour live once, on the hub, in `assets/monograph/v1/` (`monograph.css`,
`monograph.js`). Each project repo only holds its content, `docs/monograph.json`, and the
generated `docs/index.html`.

```sh
python3 tools/monograph/build.py <repo>/docs/monograph.json -o <repo>/docs/index.html
```

The script prints the derived colours: the accent fill, the text colour set on it, and the
accent used as text on paper. All three are kept at 4.5:1 or above.

## Content schema

A **text** (`T`) is either a plain string, shared by all three languages (proper names,
commands, numbers), or `{"en": …, "fr": …, "zh": …}`. Chinese is Traditional (zh-Hant).
Inline HTML is allowed: `<b>`, `<code>`, `<a href>`, `<br>`. All three languages are
mandatory; the build fails on a missing one.

| Key | Type | Notes |
|---|---|---|
| `name` | string | Project name as displayed. |
| `no` | string | Two-digit work number in the hub (`"03"`). It sets the back link (`#w03`) and the large numeral. |
| `repo` | string | `owner/name` on GitHub. Optional: leave it out for a private project, and the GitHub links are dropped. |
| `url` | string | Public URL of the page. |
| `accent` | hex | The project's colour (keep the one the old page used). |
| `meta` | object | `title`, `description` (plain strings, English, reused from the old page), optional `og_image`, `favicon` (absolute, or relative to the page), `head_extra` (raw HTML for the head, e.g. a JSON-LD block the old page had). |
| `role` | T | One line: what the thing is ("Native SwiftUI Sudoku for macOS"). |
| `thesis` | T | The old page's headline, as one sentence. |
| `lede` | T | The old page's sub-headline. |
| `actions` | list | `{label: T, href, primary?: true}`. One primary at most (Download / Install / Open). |
| `facts` | list | `{k: T, v: T}`: requirements, distribution, licence, works with… Facts only, taken from the old page. |
| `hero` | plate | Main capture (Fig. 1), shown beside the title. |
| `opener` | object | `{h: T, p?: T}`: heading on the full-bleed accent band (usually the features heading). |
| `features` | list | `{h: T, p: T or [T]}`: ruled specification rows, no icons, no emoji. |
| `chapters` | list | `{id?, h: T, p?: T, blocks: [block]}`: title on the left, blocks on the right. |
| `close` | object | `{h: T, p?: T, actions: [...]}`: last call before the colophon. |
| `colophon` | object | Optional `license: T` (default MIT), `year`, `notes: [T]`. |

A **plate** is `{src, alt: T, caption?: T, w?, h?, wide?: bool, dark?: bool}`:
- `w` and `h` are the image's intrinsic pixel size; giving them avoids layout shift.
- `dark: true` sets a dark capture on an ink plate.
- `wide: true` spans both columns of a gallery.

Plates are numbered Fig. 1, 2… in reading order.

**Blocks:**
- `{type: "p", t: T}`
- `{type: "specs", items: [{h, p}]}`
- `{type: "steps", items: [T]}`: ordered; the only numbering besides the work number.
- `{type: "pre", code: "…"}`: commands, never translated.
- `{type: "plates", items: [plate]}`
- `{type: "table", head: [T], rows: [[T]]}`
- `{type: "html", t: T}`: escape hatch, avoid.

## Rules carried over from the hub's DESIGN.md

- **No eyebrow or kicker above headings.** Old `<p class="eyebrow">` labels are dropped.
- **No emoji or Unicode glyphs as icons.** Strip them from headings and buttons.
- **No cards.** What used to be a card grid becomes `specs`, or `plates` for screenshots.
- **Sentence case** everywhere. No all-caps labels.
- **Reuse the old copy word for word.** Do not add claims; translate only what is missing.
