---
name: Vincent Lauriat — hub
description: One author's monograph of works — title page, contents, index, four cobalt-opened chapters, every project a numbered plate drawn on a construction grid.
colors:
  paper: "#eff1f2"
  plate: "#e4e7e9"
  ink: "#141414"
  ink-2: "#4d5155"
  rule: "#c2c6c9"
  grid: "#cfd3d6"
  cobalt: "#2340c8"
  on-cobalt: "#eff1f2"
typography:
  display:
    fontFamily: "Schibsted Grotesk, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, PingFang TC, Noto Sans TC, Microsoft JhengHei, sans-serif"
    fontSize: "clamp(3.4rem, 11.2vw, 11.5rem)"
    fontWeight: 500
    lineHeight: 0.88
    letterSpacing: "-0.04em"
  numeral:
    fontFamily: "Schibsted Grotesk, sans-serif"
    fontSize: "clamp(7rem, 24vw, 22rem)"
    fontWeight: 400
    lineHeight: 0.78
    letterSpacing: "-0.06em"
  headline:
    fontFamily: "Schibsted Grotesk, sans-serif"
    fontSize: "clamp(2rem, 3.6vw, 3.4rem)"
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: "-0.025em"
  section:
    fontFamily: "Schibsted Grotesk, sans-serif"
    fontSize: "clamp(1.8rem, 3.2vw, 2.8rem)"
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: "-0.02em"
  work-title:
    fontFamily: "Schibsted Grotesk, sans-serif"
    fontSize: "clamp(1.9rem, 3vw, 2.75rem)"
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: "-0.03em"
  thesis:
    fontFamily: "Schibsted Grotesk, sans-serif"
    fontSize: "clamp(1.6rem, 2.6vw, 2.4rem)"
    fontWeight: 500
    lineHeight: 1.12
    letterSpacing: "-0.02em"
  entry:
    fontFamily: "Schibsted Grotesk, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 500
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Schibsted Grotesk, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.55
  small:
    fontFamily: "Schibsted Grotesk, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
  caption:
    fontFamily: "Schibsted Grotesk, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.35
    fontFeature: "tnum"
rounded:
  none: "0"
spacing:
  gutter: "clamp(20px, 5vw, 72px)"
  column-gap: "24px"
  column-gap-phone: "16px"
  running-head: "56px"
  scroll-offset: "72px"
  touch: "44px"
  measure-max: "1440px"
components:
  running-head:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.small}"
    height: "{spacing.running-head}"
  lang-button:
    textColor: "{colors.ink-2}"
    size: "{spacing.touch}"
    padding: "0 6px"
  lang-button-active:
    textColor: "{colors.ink}"
    size: "{spacing.touch}"
    padding: "0 6px"
  contents-entry:
    textColor: "{colors.ink}"
    typography: "{typography.entry}"
    padding: "14px 0"
  contents-entry-hover:
    textColor: "{colors.cobalt}"
  index-entry:
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: "10px 0 11px"
    height: "{spacing.touch}"
  index-entry-hover:
    textColor: "{colors.cobalt}"
  chapter-opener:
    backgroundColor: "{colors.cobalt}"
    textColor: "{colors.on-cobalt}"
    padding: "clamp(56px, 10vh, 120px) 0 clamp(48px, 8vh, 96px)"
  plate:
    backgroundColor: "{colors.plate}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  work-caption:
    textColor: "{colors.ink}"
    typography: "{typography.work-title}"
  view-link:
    textColor: "{colors.ink}"
    typography: "{typography.body}"
  view-link-hover:
    textColor: "{colors.cobalt}"
  colophon:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink-2}"
    typography: "{typography.small}"
    padding: "40px 0 64px"
---

# Design System: Vincent Lauriat — hub

> **Scope.** This file records the world of **`index.html` only**, the hub surface. The project
> landing pages share a floor, `assets/base.css` (v1.0.5), which the hub also loads first. The
> hub inherits three things from that floor and overrides the rest:
>
> 1. **The trilingual mask.** Every visible string is written three times (`.en`, `.fr`, `.zh`).
>    `setLang()` puts one class on `<body>` (`lang-en` / `lang-fr` / `lang-zh`) and sets
>    `<html lang>` to `en` / `fr` / `zh-Hant`. The floor contains only *hiding* rules
>    (`display:none !important` on the two inactive languages), never display rules. The active
>    variant therefore keeps whatever display the hub layout gives it. English is the bare default
>    when no script runs.
> 2. **The ZH-Hant typographic corrections.** These are `letter-spacing:normal` on headings,
>    `line-break:strict`, and a system Han font stack. The hub re-asserts its own stack with
>    `html body.lang-zh`, so Latin glyphs stay in Schibsted Grotesk and the ideographs fall to
>    PingFang TC / Noto Sans TC / Microsoft JhengHei.
> 3. **The accessibility floor.** This covers the skip link, the `.vh` screen-reader text, the
>    reduced-motion kill switch and the 16px phone body minimum.
>
> The hub redefines the floor's `--accent` / `--on-accent` as aliases of cobalt and on-cobalt, so
> that the floor's skip link and focus ring speak the hub's one colour. It also sets
> `color-scheme: light`, overriding the floor's dark default. The floor's own dark surface tokens,
> radii, monospace face and label utilities are **not** part of this world.

## Overview

**Creative North Star: "The Architect's Monograph"**

The hub reads as one author's book of works. It opens on a title page: the author's name set
across the full measure at display scale, with "Works, since 2023" beneath it in the secondary
ink. Below that come a thesis, a lede, a one-line colophon of countable facts, and a contents
list of four chapters with roman numerals and work ranges. Next is an index of all thirty-six
works, numbered No. 01–36. Then four chapters follow. Each chapter opens on a full-bleed cobalt
page holding a huge roman numeral. After the opener, every work is presented as an
architectural plate with a caption. The plate is the project's own pictogram redrawn in ink on a
construction grid, framed by crop marks. Pictogram and caption are wrapped together in one link.

The register is daylight desk reading: cool light-grey paper, near-black ink, a secondary ink
for captions, hairline rules, and a single cobalt. Hierarchy comes from scale, weight and
position on a 12-column grid, never from ornament. There is one face, Schibsted Grotesk. It
reaches from an 11.5rem title down to 0.875rem figure captions, using weights 400, 500 and 600
only. Depth is flat. The only colour field is the cobalt chapter opener. The only motion is one
left-to-right plotter pass over each plate, the first time it enters the screen.

Density is that of a well-set book: generous margins, long vertical rests between works, and
captions held to a reading measure. The index and contents exist so that a visitor can reach a
work in one jump. The plates and captions let a reader linger.

**Key Characteristics:**
- A book structure: title page, contents, index, chapters, plates, colophon.
- Cool light-grey paper, two inks, one cobalt; no gradients, shadows or tints.
- Schibsted Grotesk only, sentence case throughout, tight negative tracking at display sizes.
- Plates are line drawings on a construction grid, with a strict three-weight stroke hierarchy.
- A 12-column grid; three alternating plate/caption layouts.
- Full-bleed cobalt chapter openers carrying a giant roman numeral.
- One motion: the plotter pass, once per plate, absent under reduced motion and without JS.

## Colors

A near-monochrome paper-and-ink palette with exactly one chromatic voice.

### Primary
- **Cobalt** (`cobalt`): the only colour in the system. It fills the chapter openers edge to
  edge. It is also the hover state of every link (work name, "View the project", plate strokes,
  contents and index entries, colophon links), the focus ring, the text-selection background and
  the favicon field. On paper and under paper-coloured text it reaches 7.0:1, so it is safe as
  text and as a fill.

### Neutral
- **Cool Paper** (`paper`): the page itself and the background of the sticky running head. It is
  a cool light grey, neither cream nor pure white. It also serves as `theme-color`.
- **Plate Grey** (`plate`): the ground of every plate, one step darker than the paper, so that a
  plate reads as a sheet laid on the page without needing a border.
- **Ink** (`ink`): text, the object stroke of every pictogram, and the full-strength rules under
  the "Contents" label, the index heading and the colophon top edge.
- **Secondary Ink** (`ink-2`): work numbers, roles, the subtitle under the author name, the
  contents numerals and ranges, figure captions, crop marks, dimension lines and inactive
  language buttons. It reaches 7.1:1 on paper and 6.4:1 on plate grey.
- **Hairline** (`rule`): divider rules between contents and index entries, and under the running
  head. It is a decorative separator only (1.5:1), so it never carries meaning alone.
- **Construction Grey** (`grid`): the 10-unit construction grid inside plates and the dashed
  construction circle.
- **Paper on Cobalt** (`on-cobalt`): text on the chapter openers. It has the same value as the
  paper, so the opener reads as the page inverted.

### Named Rules
**The One Cobalt Rule.** Cobalt is the only hue on the page. It appears as a full-bleed field in
exactly one place, the chapter opener. Everywhere else it appears only as a *response*: hover,
focus or selection. No resting text, rule or plate uses it.

**The Two Inks Rule.** Text is either ink or secondary ink, and nothing else. Meaning steps down
by moving from ink to secondary ink, never by lowering opacity or lightening further.

## Typography

**Display Font:** Schibsted Grotesk (variable 400–900, self-hosted latin subset `assets/schibsted.woff2`, preloaded, `font-display: swap`), with the Apple/Segoe/Helvetica system stack as fallback.
**Body Font:** the same face.
**CJK:** PingFang TC → Noto Sans TC → Microsoft JhengHei. The browser descends the stack glyph by glyph, so Han characters fall to the system face and Latin stays in Schibsted.

**Character:** One grotesque carries every role. Hierarchy comes from size and weight, never
from a second family, so the page looks set rather than styled. Display sizes track tightly
(−0.02 to −0.06em) and set solid; captions and body run at normal tracking.

### Hierarchy
- **Display** (500, clamp 3.4–11.5rem, line-height 0.88): the author's name on the title page
  only, spanning all 12 columns. The subtitle "Works, since 2023" sits on its own line beneath
  the name at the same size, in weight 400 and secondary ink.
- **Numeral** (400, clamp 7–22rem, line-height 0.78): the roman numeral on each chapter opener,
  in paper on cobalt, `aria-hidden`. The chapter heading carries the numeral again as
  screen-reader text.
- **Headline** (500, clamp 2–3.4rem): the chapter titles on the openers.
- **Section** (500, clamp 1.8–2.8rem): the "Index of works" heading. Its count (36) sits on the
  same baseline at body size in secondary ink, above a full ink rule.
- **Work title** (500, clamp 1.9–2.75rem; 1.5rem at ≤600px): each work's name (h3). It is
  preceded inline by its two-digit number in weight 400 and secondary ink. Long CamelCase names
  carry `<wbr>` break points.
- **Thesis** (500, clamp 1.6–2.4rem, max 20ch): the one-line thesis on the title page.
- **Entry** (500, 1.25rem): contents lines.
- **Body** (400, 1.0625rem / 1.55; 1rem at ≤600px): the lede, descriptions (max 52ch), index
  names and chapter intros (1.125rem, max 38ch). Emphasis inside descriptions uses weight 600.
- **Small** (400, 0.9375rem): the running head, the "Contents" label, the colophon line under
  the lede, and the colophon body.
- **Caption** (400, 0.875rem, tabular figures): the "Fig. N" captions under plates and the roles
  in the index.
- **Link weight** (600): the author name in the running head, "View the project", and the link
  to the index.

### Named Rules
**The Single Face Rule.** Schibsted Grotesk is the only typeface loaded. A new role is made by
choosing a size and one of the weights 400/500/600, never by adding a family. CJK uses the
system Han stack and is never given a webfont.

**The Sentence Case Rule.** Nothing is uppercased or letter-spaced open. Labels, chapter titles
and navigation are set in sentence case, at the size their role needs.

**The Tabular Number Rule.** Every work number, range and count uses tabular figures and
two-digit numbering (01–36), so that columns of numbers align like a book's index.

> ZH-Hant: the floor's `body.lang-zh h1/h2` size clamps would shrink the book's headings in Chinese;
> the hub restores its own scale for the title h1, the index heading, the chapter titles and the
> colophon headings (`html body.lang-zh …` overrides).

## Layout

The page is a single column of book sections inside a 1440px measure, with fluid side margins
of clamp(20px, 5vw, 72px). Inside each section a 12-column grid with a 24px column gap places
everything. Chapter openers break out to full bleed; their content returns to the same 12
columns.

- **Running head.** Sticky at the top, at least 56px tall, on paper with a hairline underneath.
  It holds the author name (link to top), the current chapter title (a scroll handler batched by
  `requestAnimationFrame` sets it to the section whose top has passed mid-viewport), "Index",
  the EN/FR/中文 buttons and GitHub. `scroll-padding-top: 72px` keeps anchored targets clear of
  it.
- **Title page.** The name spans all 12 columns. Below it, the thesis, lede and colophon line
  take columns 1–6, and the contents occupy columns 8–12. At ≤960px both stack full width.
- **Index of works.** A three-column list using CSS columns (minimum column width 18rem, so it
  can drop to two between breakpoints). Each entry shows number, name and role. At ≤600px it is
  forced to two columns, roles are hidden and the number column narrows.
- **Chapter opener.** The numeral takes columns 1–6 and the text columns 8–12, aligned to the
  bottom. At ≤960px both span full width.
- **Works: three plate layouts**, cycling A → B → C and restarting at A in each chapter:
  - **A (large plate left):** plate in columns 1–4, caption in 6–10.
  - **B (plate right, mirrored):** caption in 3–7, plate in 9–12.
  - **C (small plate, wide caption):** plate in 3–4, caption in 6–10.
  - **≤960px:** A and B both become plate 1–5 with caption 7–12, so the mirror exists only
    above 960px. C becomes plate 1–4 with caption 6–12.
  - **≤600px:** A stays a large plate across all columns with the caption beneath. B and C
    both become plate 1–4 with the caption beside it in 5–12. The column gap tightens to 16px.
- **Vertical rhythm.** Generous, viewport-relative rests: about clamp(56px, 8vh, 104px) between
  works and clamp(64px, 10vh, 120px) at the head of a chapter's works. Section padding scales
  with `vh` rather than stepping through a fixed scale.
- **Colophon.** Three columns (1–5, 7–9, 10–12) under a full ink rule. They stack at ≤960px.

### Named Rules
**The Grid Rule.** Every element starts and ends on one of the 12 columns. Asymmetry is created
by choosing columns, never by offsets or absolute positioning.

**The Touch Floor Rule.** Every interactive row or button is at least 44px tall, including index
entries, language buttons and running-head links.

## Elevation & Depth

The system is flat. There are no shadows, blurs or translucent layers anywhere. Depth is tonal
and bookish. A plate is a slightly darker sheet (plate grey) on the paper. A chapter is a page
turned to full cobalt. The running head is separated from the content by a hairline, not a
shadow. Stacking is limited to the sticky head (`z-index: 20`) and the skip link, which comes
from the floor.

### Named Rules
**The Printed Page Rule.** Nothing floats. If a surface needs separating, use a tonal step
(paper → plate), a rule (hairline or ink) or a full colour field, in that order of preference.

## Shapes

The form language is the right angle. No corner on the hub carries a radius: plates, openers,
rules and the focus ring (`border-radius: 0`, 2px cobalt outline, 4px offset) are all square.
Lines do the work of boxes. Hairlines divide list entries, full ink rules close headings, and no
element carries a full border.

**The plate drawing** is the system's signature geometry. It is a 240-unit square viewBox:
- **Construction grid.** A 10-unit grid in construction grey, stroke 0.5 viewBox units, on plate
  grey.
- **Crop marks.** In secondary ink, stroke 0.75 viewBox units: four corner brackets plus two
  centre ticks on the top and left edges.
- **Construction circle.** Radius 90, dashed 2 3, in construction grey, stroke 0.5.
- **Dimension lines.** Secondary ink, stroke 0.5, each with a "24" label (500 weight, 8 units)
  recording the 24-unit width and height of the source icon. They show on layouts A and B; on A
  only at ≤600px; never on C.
- **The object.** The project's own 24-unit pictogram, scaled 7.5× into the central 180-unit
  field and stroked in ink with round caps and joins. Three pictograms are solid fills instead
  of strokes.

The object stroke is a fixed **2.4 CSS px** (`vector-effect: non-scaling-stroke`), so it reads
the same on every plate size. Grid, marks, circle and dimensions are in viewBox units, so they
thin out as plates shrink. This is what keeps the hierarchy (object ≫ marks > grid) legible at
every scale.

### Named Rules
**The Stroke Hierarchy Rule.** There are three line weights, never more: the object at 2.4px
non-scaling, the crop marks at 0.75, and the grid, circle and dimensions at 0.5. A new plate
redraws the project's real icon. It never uses a stock glyph, and never fills its grid with
decoration.

## Components

### Running head
Quiet and always present. It sits on paper with a hairline underneath and small type. The author
name is in weight 600; the chapter label is in secondary ink, truncated with an ellipsis.
"Index" and GitHub underline on hover (4px offset). At ≤600px the chapter label and GitHub are
hidden.

### Language buttons
Three borderless text buttons (EN, FR, 中文), each at least 44×44px. Inactive buttons are in
secondary ink. The active button is in ink with a 2px underline at a 6px offset, and carries
`aria-pressed`. Hovering an inactive button turns it to ink. The choice persists in
`localStorage` (key `vl-lang`) and otherwise follows the browser language.

### Contents
The "Contents" label sits in small secondary ink above a full ink rule. Each entry is a link laid
out as a three-column row: roman numeral (secondary ink, 400), chapter title (500, 1.25rem) and
work range (secondary ink, tabular). Entries are separated by hairlines. On hover the title turns
cobalt. Below the list, an underlined link in weight 600 leads to the index; its authored arrow
is rotated 90° to point down.

### Index entry
A row at least 44px tall: two-digit number (secondary ink, tabular, spanning both lines), name
(500), and role beneath it (caption size, secondary ink). Rows are separated by hairlines and
never break across columns. On hover the name turns cobalt. Each entry links to its work's
anchor (`#w01`–`#w36`).

### Chapter opener (signature)
A full-bleed cobalt page at the head of each chapter. The giant roman numeral is set
bottom-aligned, with paper-coloured text beside it: the chapter title (headline), the count line
("12 works · No. 01–12"), and a one-sentence intro. "No." is left untranslated in all three
languages, as a bibliographic convention.

### Work: plate + caption (signature)
Each work is an `<article>` containing **one** link that wraps both the plate (a `<figure>`
holding the drawing and a "Fig. N" caption) and the caption block. The caption block holds the
name (h3) with its number inline, the role in secondary ink, the description, and "View the
project" in weight 600, underlined (1px, 5px offset), followed by an authored 16-unit SVG arrow
(stroke 1.6, round caps). On hover, the name, the link and every pictogram stroke or fill turn
cobalt at once. The plate ground, grid and marks stay unchanged. The hover has no transition, and
keyboard focus (`:focus-visible`) applies the same recolour plus the cobalt outline.

### Plotter pass (motion)
This is the only motion in the system. When a plate first comes within 85% of the viewport
height, its pictogram is revealed left to right by a `clip-path` inset sweep (1.3s,
cubic-bezier(.65, 0, .35, 1)), as if a plotter head drew it once. Only the object is clipped;
grid, marks and dimensions are already on the sheet. The pass is applied only to plates that are
below the fold at load. It runs only when JavaScript runs and reduced motion is not requested;
otherwise every plate is simply drawn. The same scroll handler drives the running-head chapter
label, so the page has one passive listener, batched by `requestAnimationFrame`.

### Colophon
A footer under a full ink rule, in three columns: Colophon (facts of making), Elsewhere (links)
and Type & drawings (credits and ©). Headings are 1.25rem, body text is small in secondary ink,
and links are in ink, turning cobalt on hover.

## Do's and Don'ts

### Do:
- **Do** keep cobalt (#2340c8) as the single hue: full-bleed on chapter openers, and otherwise only as hover, focus and selection.
- **Do** set every new role in Schibsted Grotesk at weight 400, 500 or 600, in sentence case.
- **Do** number works with two tabular digits and keep the index, the contents ranges and the chapter count lines in agreement.
- **Do** draw every new plate from the project's own 24-unit icon, scaled 7.5× into the 240 viewBox, with the object at 2.4px non-scaling stroke over the shared grid, crop marks and circle.
- **Do** wrap each work's plate and caption in a single link, and place them on the 12-column grid using the A/B/C layouts in sequence.
- **Do** write every visible string three times (`.en`, `.fr`, `.zh`) and let the body class decide which one shows.
- **Do** keep interactive rows at least 44px tall and the focus ring a square 2px cobalt outline.
- **Do** keep plates fully visible without JavaScript and under reduced motion; the plotter pass is an enhancement.

### Don't:
- **Don't** add a second typeface, a monospace face, or a webfont for CJK.
- **Don't** introduce shadows, gradients, translucent overlays or rounded corners.
- **Don't** add a second accent or per-project colours on the hub.
- **Don't** uppercase or letter-space labels, or place small category labels (kickers) above headings; the one label on the page is the "Contents" heading of the contents list.
- **Don't** use glyph or emoji arrows; arrows are authored SVG paths that inherit `currentColor`.
- **Don't** add a fourth stroke weight to the plates or fill their grid with decoration.
- **Don't** animate anything other than the plotter pass, and never replay it.
- **Don't** add photographs, screenshots or raster images to the page.
