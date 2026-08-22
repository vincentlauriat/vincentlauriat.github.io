---
name: Vincent Lauriat — hub
description: One builder's flight case — 28 die-cut vinyl stickers accreted on scuffed black laminate, framed in riveted aluminium.
colors:
  case-laminate: "#16130f"
  stencil-beige: "#d9cfb6"
  stencil-dim: "#a2977c"
  vinyl-white: "#f0e9d8"
  sticker-ink: "#17130d"
  caution-yellow: "#e8b90f"
  manifest-paper: "#ece4cf"
  paper-ink: "#23201a"
  stamp-red: "#c8352b"
typography:
  display:
    fontFamily: "Saira Stencil One, sans-serif"
    fontSize: "clamp(2.4rem, 5.6vw, 4.4rem)"
    fontWeight: 400
    lineHeight: 1.02
    letterSpacing: "0.015em"
  block:
    fontFamily: "Archivo Black, Arial Black, sans-serif"
    fontSize: "1.02rem"
    fontWeight: 400
    lineHeight: 1.05
  mark:
    fontFamily: "Permanent Marker, Comic Sans MS, cursive"
    fontSize: "1.18rem"
    fontWeight: 400
  type:
    fontFamily: "Courier Prime, Courier New, monospace"
    fontSize: "clamp(0.95rem, 1.6vw, 1.05rem)"
    fontWeight: 400
    lineHeight: 1.75
rounded:
  die: "18px"
  chip: "7px"
  plate: "10px"
  paper: "3px"
spacing:
  gutter: "28px"
  sticker-pad: "20px 16px"
  field-gap-mobile: "22px 16px"
components:
  sticker:
    textColor: "{colors.sticker-ink}"
    rounded: "{rounded.die}"
    padding: "20px 16px"
  lang-chip:
    backgroundColor: "{colors.vinyl-white}"
    textColor: "{colors.sticker-ink}"
    rounded: "{rounded.chip}"
    padding: "8px 12px"
  lang-chip-active:
    backgroundColor: "{colors.caution-yellow}"
    textColor: "{colors.sticker-ink}"
    rounded: "{rounded.chip}"
    padding: "8px 12px"
  manifest:
    backgroundColor: "{colors.manifest-paper}"
    textColor: "{colors.paper-ink}"
    rounded: "{rounded.paper}"
    padding: "56px 54px 48px"
---

# Design System: Vincent Lauriat — hub (the flight case)

> Scope: this file records the world of **`index.html` only** (the hub surface). The 14 project
> landing pages live in other repos on a different, shared floor — `assets/base.css` v1.0.5 —
> which this world **inherits unchanged** (tokens `--accent`/`--on-accent`, the trilingual
> EN/FR/ZH-Hant masking mechanism, and the a11y floor). base.css is documented there, not here;
> whether the landing pages ever adopt case-world tokens is explicitly unresolved.
> Direction contract: HTML comment, first child of `<body>` (seed 39f91a6c, user-locked).

## Overview

**Creative North Star: "The Flight Case"**

The hub is not a page about a portfolio; it is one physical object — a road case owned by one
builder, photographed straight-on. Black scuffed laminate, riveted aluminium extrusion rails and
corner braces framing the viewport, and years of die-cut vinyl stickers accreted on the lid: 28
stickers, one per shipped project, each carrying its project's own accent color inside a white
vinyl border. Depth is chronology — the newest stickers sit highest in the stack and shine, the
oldest have yellowed and bleached. Facts print on a strip of yellow caution tape; findability
lives in a typewritten packing manifest taped to the case; the footer is a riveted spec plate.
It refuses the dev-portfolio card grid entirely.

Every texture is authored in CSS/SVG — the laminate scratches are repeating-linear-gradients,
the grain is an inline SVG turbulence data-URI, the handle and braces are inline SVG. Zero
external images, zero frameworks. Where the world's mess and the catalog's job conflict,
**clarity wins**: sticker names stay legible, and the manifest — not the sticker field — is the
screen-reader and findability backbone.

**Key Characteristics:**
- One object, not a layout: fixed aluminium frame, laminate ground, accreted stickers.
- Depth = time: z-index and fading (`age-0`…`age-3`) encode shipping chronology together.
- Four lettering voices (stencil, block, marker, typewriter), zero system display faces.
- One motion: the sticker corner peel. Nothing else moves for decoration.
- All claims printed on the case are factual and countable.

## Colors

A warm, sun-faded hardware palette: near-black laminate, adhesive-beige stencils, vinyl white,
one loud caution yellow — plus 28 per-project accents that arrive with the stickers, not from
this palette.

### Primary
- **Caution Yellow** (`--tape-y`): the case's only loud voice — the caution-tape facts band,
  the active language sticker, `::selection`, and (as `--accent`) the base.css focus ring and
  skip link. `--on-accent` is overridden to `#17130d` (dark ink) so text on yellow stays legible.

### Secondary
- **Stamp Red** (`--red`): the manifest's rubber-stamp "ALL SHIPPED" and the manifest row hover
  wash (`rgba(200,53,43,.09)`). Paper-world only; it never appears on the laminate.

### Neutral
- **Case Laminate** (`--case`): the ground. Warm near-black, always seen through the scratch
  layers and grain; also the "case showing through" color inside the peel gradient.
- **Stencil Beige** (`--stencil`): default text on the case — the spray-stencil/adhesive-residue
  color. Headline, signature, zone marks (dimmed via `--stencil-dim` `#a2977c`).
- **Vinyl White** (`--vinyl`): the 5px die-cut border of every sticker, and the resting
  background of control stickers (language chips, GH sticker).
- **Sticker Ink** (`--ink`): dark ink on light sticker faces and on yellow; default `--sink`.
- **Manifest Paper** (`--paper`) / **Paper Ink** (`--paper-ink`): the taped inventory sheet —
  the one light surface in the world, with its own ink.

### Named Rules
**The Sticker-Owns-Its-Color Rule.** Project accents (`--c`, set inline per sticker) come from
each project's own landing-page identity; the hub palette never dictates them. Ink on a sticker
is always dark (`--sink` defaults to `--ink`); never white text on an accent.
**The One Loud Voice Rule.** Caution yellow is the only saturated color the case itself speaks.
Everything else on the laminate is beige, alu, or near-black.
**The Paper World Rule.** Red exists only on paper (manifest); paper colors never leak onto the
laminate, and laminate beige never appears on paper.

## Typography

**Display Font:** Saira Stencil One (stencil — the case marking voice)
**Block Font:** Archivo Black (die-cut sticker lettering, tape values)
**Script Font:** Permanent Marker (hand-lettered sticker voice)
**Typewriter Font:** Courier Prime 400/700 (lede, manifest, sublabels, footer plate)

**Character:** four vernacular print voices, all Google-Fonts loaded (non-blocking `media="print"`
swap trick with `<noscript>` fallback), each with a real fallback stack. No system display face
ever carries a title — except in ZH, where `body.lang-zh h1` deliberately falls back to
`--font-sans` at weight 800 because stencil glyphs don't exist for Han characters.

### Hierarchy
- **Display / h1** (400, `clamp(2.4rem, 5.6vw, 4.4rem)`, lh 1.02): stencil, uppercase,
  `letter-spacing: .015em`, `text-shadow: 0 2px 0 rgba(0,0,0,.5)`. Second clause dimmed with
  `--stencil-dim` inside the same h1.
- **Sticker name `.nm`** (1.02rem base; 1.3rem on `.lead`; 1.18rem in marker voice): voice set
  per sticker by `f-block` (uppercase), `f-sten` (uppercase, +.06em), or `f-mark`.
- **Sublabel `.sub`** (Courier 700, .62rem, +.13em, uppercase): the sticker's one-line role.
- **Lede** (Courier, `clamp(.95rem, 1.6vw, 1.05rem)`, lh 1.75, max 58ch, color `#b7ad93`).
- **Manifest** (everything Courier): h2 1.15rem +.22em uppercase; zone h3 .82rem +.2em with
  dotted leader line; rows .88rem with bold `.ref`/`.pname`.
- **Stencil marks** (`.case-mark` .78rem +.26em; `.zone-mark` .8rem +.3em): uppercase,
  `--stencil-dim`, always slightly rotated.

### Named Rules
**The Four Voices Rule.** Every piece of text speaks in exactly one of the four voices; the
voice varies per sticker (part of the accretion's irregularity) but never mixes inside one
sticker name.
**The ZH Exception Rule.** Chinese never uses the stencil face; it takes `--font-sans` at 800
(hub override) plus base.css's ZH sizing/line-breaking floor. Nothing may degrade in FR or ZH.

## Layout

One centered column: `.wrap` at `max-width: 1240px`, 28px gutters. The viewport is framed by
fixed chrome — four 10px aluminium `.rail`s (z-60) and four 56×56 SVG corner `.brace`s (z-61) —
that never scrolls. Vertical order: nav (signature + language stickers + GH sticker) → hero grid
(`minmax(0,1.25fr) minmax(0,.75fr)`: stencil headline + typewriter lede left, recessed-handle
SVG right) → caution tape angled −1.4° → stencil case-mark → the sticker field → the manifest →
the riveted plate.

**The field** (`.field`) is the world's core layout: at ≥761px it is a fixed-height
(`--field-h`, 1310px) relative canvas where every sticker is absolutely placed by inline
`--x/--y/--r/--w/--z` custom properties — a hand-composed accretion, denser at the top, with
`.zone-mark` stencils painted between clusters and two `.ghost` residues in the gaps.

**Responsive** (world-preserving, not grid-reflowing):
- ≤900px: hero collapses to one column; handle centers below at 220px.
- ≤760px: the accretion **recompacts** — the field becomes wrapped flex (`gap: 22px 16px`),
  stickers keep their rotation and shape but abandon absolute positions
  (`width: clamp(140px, 44vw, 210px)`, lead `min(320px, 92vw)`); zone marks become full-width
  centered dividers; the manifest drops its rotation and its rows restack to a 2-row grid.
- ≤430px: sticker names clamp (.84rem, `overflow-wrap: anywhere`), sublabels shrink to .56rem.

### Named Rules
**The Chronology-Is-Depth Rule.** Stacking is meaning: `--z` rises with recency (lead sticker
`--z:40`, freshest 30–39, oldest 5–9) and always pairs with the matching `age-*` class. A new
sticker goes on top; never re-sort the pile alphabetically or by grid.
**The Recompaction Rule.** Below 761px the accretion flows but stays an accretion: rotations
and die-cut shapes survive; only the coordinates die.

## Elevation & Depth

Depth is physical, not tonal: every layer casts a soft dark drop shadow onto the laminate, and
lifting is the hover language. No glows, no colored shadows, no blur-behind.

### Shadow Vocabulary
- **Sticker at rest** (`0 3px 10px rgba(0,0,0,.55), 0 1px 0 rgba(255,255,255,.12) inset`):
  vinyl sitting on laminate; the inset line is the vinyl edge catching light.
- **Sticker lifted** (`0 14px 30px rgba(0,0,0,.65)` + `translateY(-5px) scale(1.03)`, `z-index:55`):
  hover/focus-visible — the sticker comes off the case toward you.
- **Tape** (`0 6px 16px rgba(0,0,0,.5)`), **manifest** (`0 18px 44px rgba(0,0,0,.6)`),
  **plate** (`0 8px 20px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.5)`),
  **handle** (`drop-shadow(0 10px 22px rgba(0,0,0,.65))`), **rails** (inset + `0 0 10px` dark).
- **Grain everywhere**: the shared `--grain` SVG-turbulence data-URI layers over the body, the
  tape, the manifest, and each sticker (`::after`, `mix-blend-mode: overlay`, opacity keyed to age).

### Motion (lives here because it *is* the depth grammar)
**The One Peel Rule.** The world has exactly one motion idea: the peel. On sticker
hover/focus-visible, the top-right corner curls (`::before` scales 0→1 from `top right`) and the
sticker lifts. Easing is ease-out-quint `cubic-bezier(.22, 1, .36, 1)` at .22s; secondary state
transitions (language-chip filters .18s ease, manifest arrow nudge .2s ease) stay under .25s.
No entrance animations, no parallax, no loops. `prefers-reduced-motion` is honored by base.css's
global kill switch; `.lifted` gives one old sticker a *permanently* peeled corner — a static
state, not an animation.

## Shapes

The form language is **die-cutting**: every interactive object is a cut vinyl shape with a 5px
`--vinyl` border, its silhouette set by the `--shape` custom property (default 18px):

- `.s-round` — `50%` + `aspect-ratio: 1` (circular die)
- `.s-pill` — `999px`
- `.s-tab` — `14px 14px 40px 14px` (one drooping corner)
- `.s-arch` — `48% 48% 12px 12px` (arched top)
- `.s-slant` — `6px 26px 6px 26px` (parallelogram-feel corners)
- default die — `18px` rounded rectangle (what `.s-badge`-tagged stickers actually render as; see
  the not-canonized note)

Everything is slightly rotated — stickers ±2–7°, tape −1.4°, manifest +.4°, stamp −6°, chips
±2–3° — nothing in the world sits at exactly 0° except the frame and the manifest rows.
Hard-edged machine parts (rails, braces, sep bars, tape's 3px dark borders) contrast the soft
die-cuts; the tape's ragged ends are a `clip-path` polygon. Ghosts reuse the die silhouette at
`border: 5px rgba(240,233,216,.14)` — the outline of a sticker that was torn off.

**The Never-Square Rule.** Anything stuck onto the case carries both a rotation and a die-cut
radius. Only the case's own machined parts (rails, braces, separators) may be perfectly straight.

## Components

### Die-cut sticker (`.stk`) — the signature component
- **Anatomy:** `<a>` with icon (`.ic`, 40px inline SVG, `stroke="currentColor"` 1.9), name
  (`.nm`), sublabel (`.sub`); centered column, `min-height: 44px` touch floor.
- **Per-sticker API (inline style):** `--c` (project color), `--x/--y` (desktop position),
  `--r` (rotation), `--w` (width), `--z` (chronology), optional `--sink` (ink override).
- **Classes:** one shape (`s-*`), one voice (`f-*`), one age (`age-0`…`age-3`); `.lead` for the
  single freshest flagship (bigger padding, 1.3rem name, `--z:40`); `.lifted` for a permanently
  peeled corner.
- **Aging:** `age-3` = `saturate(.45) sepia(.55) brightness(.88) contrast(.92)` + grain at .75;
  down to `age-0` = `filter: none`. Sunfade is a filter, never a different `--c`.
- **Hover/focus:** the peel (see Elevation & Depth). Focus ring comes from base.css.

### Ghost (`.ghost`)
Adhesive residue where a sticker was torn off: die-cut silhouette, translucent vinyl border,
grain-and-radial residue fill, `pointer-events: none`, `aria-hidden`. Placed sparsely (2 on the
shipped page) to prove the accretion is alive. Never interactive, never carries text.

### Language toggle (`.langtog`) & GH link (`.ghlink`)
Controls are stickers too. Three vinyl chips (7px radius, ±2–3° rotations, 44px min targets);
inactive chips are sun-faded via `filter: saturate(.45) sepia(.28) brightness(.82)`, the active
one is a fresh caution-yellow sticker, un-faded, lifted 1px, `aria-pressed`. The GitHub link is
a round marker-voice sticker rotated 6°. State change = filter/lift only.

### Caution tape (`.tape`)
The facts band: yellow gradient + 45° hazard striping + grain, 3px near-black top/bottom
borders, ragged `clip-path` ends, rotated −1.4°. Cells are Archivo Black value + Courier 700
uppercase label, separated by 2px dark `.sep` bars. Facts on the tape are countable and true;
`role="group"` with a localized `aria-label`.

### Stencil marks (`.case-mark`, `.zone-mark`)
Spray-stencil paint directly on the laminate: Saira Stencil One, uppercase, wide tracking,
`--stencil-dim`, slight rotation, `pointer-events: none`. Zone marks label sticker clusters
("AI / DEV — 07"); they are decorative (`aria-hidden`) — the manifest carries the real structure.

### Manifest (`.manifest`, `.mrow`)
The typewritten inventory taped to the case (max-width 1080px, rotated .4°, two translucent tape
strips via `::before/::after`, ruled-paper line gradient, grain). Zones A–D with dotted-leader
h3s; rows are a `64px 178px 1fr 34px` baseline grid (ref / name / description / arrow), hover =
red wash + 4px arrow nudge. Every sticker has a manifest row; the manifest — not the field — is
the catalog backbone and the screen-reader path. Red stamp top-right, rotated −6°.

### Footer plate (`footer .plate`)
Brushed-alu gradient plate, 10px radius, four radial-gradient rivet dots in the corners, Courier
700 uppercase copy, dark-red underlined links, `EST. MMXXIII` engraving line.

### Frame (`.rail`, `.brace`)
Fixed chrome: 10px aluminium gradient rails on all four edges (z-60) and 56px riveted SVG corner
braces (z-61), all `aria-hidden`, drawn with literal gradient stops (`#8d887e→#f2eee4→#7c776d`).
The frame is the one part of the world that never scrolls, tilts, or reacts.

## Do's and Don'ts

### Do:
- **Do** add a new project as sticker + manifest row **together**, and bump the tape counts, the
  zone counts, `--field-h`, and the meta/og descriptions in the same change (the counting rule
  lives in the HTML comment above `.tape`).
- **Do** put a new sticker **on top**: `age-0`, `filter: none`, a `--z` above the current
  maximum, positioned in its zone's cluster; demote the previous `.lead` if the newcomer is the
  flagship.
- **Do** give every sticker one shape class, one voice class, one age class, a project `--c`
  with dark ink, a 40px stroke icon, and the 5px vinyl border.
- **Do** keep all texture authored in CSS/SVG (`--grain`, scratch gradients, inline SVG) — zero
  external images.
- **Do** keep every visible string trilingual (`.en/.fr/.zh` spans) and every control at
  ≥44px — the base.css floor is binding and WCAG AA may not regress.

### Don't:
- **Don't** reflow the field into a uniform grid, equalize sticker sizes, or zero the rotations
  — the irregular accretion *is* the identity; clarity is won by legible names and the manifest,
  not by tidying the pile.
- **Don't** add a second motion idea. The peel (ease-out-quint, ≤.25s) is the entire grammar;
  no entrance animations, parallax, marquees, or hover glows.
- **Don't** write light text on an accent or on yellow — ink on stickers and tape is always
  dark (`--ink` / `--on-accent: #17130d`).
- **Don't** let paper and laminate worlds bleed: no red on the case, no stencil-beige text on
  the manifest, no cool base.css surface colors (`#0a0c12` family) anywhere on this page.
- **Don't** print a claim the corpus can't count — facts on tape, stamp, and plate stay factual
  ("21 instruments", "0 telemetry", "signed & notarized"; apps are EN/FR only — never promise
  ZH for the apps).
