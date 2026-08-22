# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary: Mac users looking for useful native utilities — they arrive from search, GitHub, or a project README, scan the catalog, open a project page, download. Secondary (confirmed): peers and recruiters reading the hub as a technical calling card; the page must read as serious craftsmanship without turning into a résumé.

## Product Purpose

The hub is the front door to Vincent Lauriat's software corpus: 21 native macOS apps (signed, notarized, Swift), 4 games, plus AI/dev tools. Success = a visitor finds the relevant project fast and clicks through to its landing page; secondary success = the visitor leaves convinced of the build quality.

## Positioning

One person ships a full rack of native, notarized, open-source macOS instruments that surface what the system measures but hides — no telemetry, no cloud accounts, MIT licensed. A neighboring portfolio cannot truthfully copy the breadth (25 shipped projects) or the "signed & notarized, 100% Swift" floor.

## Operating Context

- Static GitHub Pages site, one `index.html` + shared `assets/base.css` (v1.0.5) reused by the 14 project landing pages. No build step, no framework.
- Each project card links to its own landing page (same corpus, own accent color).
- Counting rule for hero claims documented in `index.html` comment: 21 = native Swift macOS apps; games, OpenAlice, HomebrewConfig, Toolkit excluded.

## Capabilities and Constraints

- **Binding**: trilingual EN/FR/ZH-Hant via the `setLang()` body-class mechanism; every visible string carries three variants. (User-confirmed untouchable, 2026-08-22.)
- Free to change (explicitly not pinned by user): current card copy and headline, single-file structure and base.css coupling, category bands, per-project accent colors.
- Factual claims stay factual: counts, "signed & notarized", "no telemetry", license, localization scope (apps EN/FR only — never promise ZH for the apps).
- No JS frameworks; page must remain fast and dependency-light on GitHub Pages.

## Brand Commitments

- Name: "Vincent Lauriat" as signature; corpus tone is factual, instrument-precise, no marketing hyperbole.
- **Binding aesthetic constraint (user, 2026-08-22, redesign brief)**: "un look plus moderne qui fasse pas IA, classe et raffiné" — modern, must not read as AI-generated design, classy and refined.

## Evidence on Hand

- 25 real shipped projects with landing pages under `vincentlauriat.github.io/<Project>/`.
- Real facts: 21 native Swift apps, 0 telemetry, MIT, EN/FR app localization, macOS 13+, signed & notarized.
- Assets: `assets/favicon.svg`, `assets/og.png` (2026-08-22). No photography, no testimonials — do not fabricate any.

## Product Principles

1. The catalog is the product: findability of the right project beats self-presentation.
2. Every claim on the page is countable and true; precision is the brand.
3. The hub sets the quality bar visitors expect from the apps themselves.
4. Three languages are first-class; nothing may degrade in FR or ZH-Hant.
5. Zero-dependency speed is part of the craft message.

## Accessibility & Inclusion

WCAG AA floor already achieved (contrast ≥4.5:1, unique link names, full heading hierarchy, 44px touch targets, reduced-motion respected); the redesign may not regress it.
