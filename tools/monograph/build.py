#!/usr/bin/env python3
"""Génère une fiche monographie (landing page) à partir d'un fichier de contenu JSON.

    python3 tools/monograph/build.py content.json  -o <repo>/docs/index.html

Le contenu est la seule source : textes, captures, faits. La mise en page et le
style vivent dans assets/monograph/v1/ du hub. Un texte est soit une chaîne
(identique dans les trois langues : noms propres, commandes), soit un objet
{"en":…, "fr":…, "zh":…}. Le HTML en ligne (<b>, <code>, <a>) est permis.
Voir tools/monograph/README.md pour le schéma complet.
"""
import argparse, colorsys, html, json, sys

PAPER = "#eff1f2"
INK = "#141414"
KIT = "/assets/monograph/v1"
HUB = "https://vincentlauriat.github.io/"
LANGS = ("en", "fr", "zh")
ARW = '<svg class="arw{c}" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4"/></svg>'


# ── couleur ───────────────────────────────────────────────────────────────
def _rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def _hex(rgb):
    return "#" + "".join(f"{round(max(0, min(1, c)) * 255):02x}" for c in rgb)


def lum(h):
    def ch(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in _rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def darken_until(h, ok):
    """Descend la luminosité (teinte et saturation gardées) jusqu'à ok(couleur)."""
    hh, ll, ss = colorsys.rgb_to_hls(*_rgb(h))
    while ll > 0 and not ok(_hex(colorsys.hls_to_rgb(hh, ll, ss))):
        ll -= 0.005
    return _hex(colorsys.hls_to_rgb(hh, max(ll, 0), ss))


def accent_set(accent):
    """aplat, texte sur l'aplat, et la couleur en texte sur le papier — tout ≥ 4.5:1."""
    fill = accent
    on = INK if contrast(fill, INK) >= contrast(fill, PAPER) else PAPER
    if contrast(fill, on) < 4.5:
        fill = darken_until(fill, lambda c: contrast(c, PAPER) >= 4.5)
        on = PAPER
    ink = darken_until(accent, lambda c: contrast(c, PAPER) >= 4.6)
    return fill, on, ink


# ── texte ─────────────────────────────────────────────────────────────────
def T(v, tag="span"):
    """Rend un texte trilingue. Une chaîne simple est commune aux trois langues."""
    if v is None:
        return ""
    if isinstance(v, str):
        return v
    miss = [l for l in LANGS if not v.get(l)]
    if miss:
        sys.exit(f"texte incomplet ({', '.join(miss)} manquant) : {v}")
    return "".join(f'<{tag} class="{l}">{v[l]}</{tag}>' for l in LANGS)


def plain(v, lang="en"):
    s = v if isinstance(v, str) else v[lang]
    import re
    return html.escape(re.sub(r"<[^>]+>", "", s), quote=True)


def esc(s):
    return html.escape(s, quote=True)


UI = {
    "back": {"en": "Vincent Lauriat", "fr": "Vincent Lauriat", "zh": "Vincent Lauriat"},
    "skip": {"en": "Skip to content", "fr": "Aller au contenu", "zh": "跳至內容"},
    "fig": {"en": "Fig.", "fr": "Fig.", "zh": "圖"},
    "work": {"en": "Work no.", "fr": "Réalisation n°", "zh": "作品編號"},
    "in_book": {"en": "in the works of Vincent Lauriat", "fr": "dans les réalisations de Vincent Lauriat",
                "zh": "收錄於 Vincent Lauriat 作品集"},
    "all": {"en": "All works", "fr": "Toutes les réalisations", "zh": "全部作品"},
    "source": {"en": "Source", "fr": "Source", "zh": "原始碼"},
    "about": {"en": "About this page", "fr": "À propos de cette page", "zh": "關於本頁"},
    "about_p": {"en": "Set in Schibsted Grotesk, on the grid of the book it belongs to.",
                "fr": "Composée en Schibsted Grotesk, sur la grille du livre auquel elle appartient.",
                "zh": "以 Schibsted Grotesk 排版，沿用其所屬作品集的網格。"},
}


# ── blocs ─────────────────────────────────────────────────────────────────
class Figs:
    n = 0


def figure(p, figs):
    figs.n += 1
    cls = "plate" + (" ink" if p.get("dark") else "") + (" wide" if p.get("wide") else "")
    w = f' width="{p["w"]}" height="{p["h"]}"' if p.get("w") else ""
    load = "" if figs.n == 1 else ' loading="lazy"'
    cap = p.get("caption")
    capt = f'<figcaption><span class="fg">{T(UI["fig"])} {figs.n}</span>{T(cap)}</figcaption>' if cap else \
        f'<figcaption><span class="fg">{T(UI["fig"])} {figs.n}</span></figcaption>'
    return (f'<figure class="{cls}"><div class="pl"><img src="{esc(p["src"])}" alt="{plain(p["alt"])}"'
            f'{w}{load} decoding="async"></div>{capt}</figure>')


def specs(items):
    li = []
    for it in items:
        body = "".join(f"<p>{T(x)}</p>" for x in (it["p"] if isinstance(it["p"], list) else [it["p"]]))
        li.append(f'<li><h3>{T(it["h"])}</h3><div>{body}</div></li>')
    return f'<ul class="specs">{"".join(li)}</ul>'


def block(b, figs):
    t = b["type"]
    if t == "p":
        return f"<p>{T(b['t'])}</p>"
    if t == "specs":
        return specs(b["items"])
    if t == "steps":
        return '<ol class="steps">' + "".join(f"<li><p>{T(x)}</p></li>" for x in b["items"]) + "</ol>"
    if t == "pre":
        return f"<pre><code>{esc(b['code'])}</code></pre>"
    if t == "plates":
        return '<div class="plates">' + "".join(figure(p, figs) for p in b["items"]) + "</div>"
    if t == "table":
        head = "".join(f"<th>{T(h)}</th>" for h in b["head"])
        rows = "".join("<tr>" + "".join(f"<td>{T(c)}</td>" for c in r) + "</tr>" for r in b["rows"])
        return f'<div class="tbl-wrap"><table class="tbl"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
    if t == "html":
        return T(b["t"])
    sys.exit(f"bloc inconnu : {t}")


def actions(acts):
    out = []
    for a in acts:
        if a.get("primary"):
            out.append(f'<a class="btn" href="{esc(a["href"])}">{T(a["label"])}</a>')
        else:
            out.append(f'<a class="lnk" href="{esc(a["href"])}">{T(a["label"])}{ARW.format(c="")}</a>')
    return '<div class="acts">' + "".join(out) + "</div>"


def chapter(c, figs):
    hp = f"<p>{T(c['p'])}</p>" if c.get("p") else ""
    body = "".join(block(b, figs) for b in c["blocks"])
    cid = f' id="{c["id"]}"' if c.get("id") else ""
    return (f'<section class="chapter"{cid}><div class="wrap g12"><div class="ch-head"><h2>{T(c["h"])}</h2>{hp}</div>'
            f'<div class="ch-body">{body}</div></div></section>')


# ── page ──────────────────────────────────────────────────────────────────
def build(d):
    fill, on, ink = accent_set(d["accent"])
    figs = Figs()
    repo = d["repo"]
    gh = f"https://github.com/{repo}"
    name = d["name"]
    no = d["no"]
    meta = d["meta"]

    langs = "".join(f'<button type="button" data-lang="{l}" aria-pressed="false">{lab}</button>'
                    for l, lab in (("en", "EN"), ("fr", "FR"), ("zh", "中文")))

    facts = ""
    if d.get("facts"):
        facts = '<dl class="facts">' + "".join(
            f"<div><dt>{T(f['k'])}</dt><dd>{T(f['v'])}</dd></div>" for f in d["facts"]) + "</dl>"

    hero = figure(d["hero"], figs) if d.get("hero") else ""

    op = d["opener"]
    opener = (f'<section class="opener" id="content"><div class="wrap"><div class="op-grid">'
              f'<div class="numeral" aria-hidden="true">{no}</div>'
              f'<div class="op-text"><h2>{T(op["h"])}</h2>{"<p>" + T(op["p"]) + "</p>" if op.get("p") else ""}</div>'
              f'</div></div></section>')
    feats = f'<section class="chapter"><div class="wrap">{specs(d["features"])}</div></section>' if d.get("features") else ""

    chapters = "".join(chapter(c, figs) for c in d.get("chapters", []))

    cl = d["close"]
    close = (f'<section class="close"><div class="wrap g12"><h2>{T(cl["h"])}</h2>'
             f'<div class="c-r">{"<p>" + T(cl["p"]) + "</p>" if cl.get("p") else ""}{actions(cl["actions"])}</div>'
             f'</div></section>')

    col = d.get("colophon", {})
    lic = T(col.get("license", {"en": "MIT License", "fr": "Licence MIT", "zh": "MIT 授權"}))
    extra = "".join(f"<p>{T(x)}</p>" for x in col.get("notes", []))
    colophon = (f'<footer class="colophon"><div class="wrap g12">'
                f'<div class="c1"><h2>{name}</h2><p>{T(UI["work"])} <span class="num">{no}</span> {T(UI["in_book"])}.</p>'
                f'<p><a href="{HUB}#w{no}">{T(UI["all"])}</a></p></div>'
                f'<div class="c2"><h2>{T(UI["source"])}</h2><p><a href="{gh}">github.com/{repo}</a></p><p>{lic} · © {col.get("year", "2026")} Vincent Lauriat</p>{extra}</div>'
                f'<div class="c3"><h2>{T(UI["about"])}</h2><p>{T(UI["about_p"])}</p></div>'
                f'</div></footer>')

    title = plain(meta["title"])
    desc = plain(meta["description"])
    og = meta.get("og_image", "")
    icon = meta.get("favicon", "")
    head_extra = meta.get("head_extra", "")

    return f"""<!DOCTYPE html>
<html lang="en" style="--accent:{fill};--on-accent:{on};--accent-ink:{ink}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="{PAPER}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{esc(d.get('url', ''))}">
{f'<meta property="og:image" content="{esc(og)}">' if og else ''}
<meta name="twitter:card" content="summary_large_image">
{f'<link rel="icon" href="{esc(icon)}">' if icon else ''}
<link rel="preload" href="/assets/schibsted.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{KIT}/monograph.css">
{head_extra}
</head>
<body>
<a class="skip" href="#content">{T(UI["skip"])}</a>
<header class="running"><div class="wrap">
<a class="back" href="{HUB}#w{no}">{ARW.format(c=" l")}{T(UI["back"])}</a>
<span class="here"><span class="num">{no}</span> · {name}</span>
<div class="langs" role="group" aria-label="Language / Langue / 語言">{langs}</div>
<a class="gh" href="{gh}">GitHub</a>
</div></header>
<main>
<section class="title"><div class="wrap g12">
<h1 class="nm{" long" if len(name) > 11 else ""}" style="--len:{len(name)}"><span class="no" aria-label="{plain(UI['work'])} {no}">{no}</span><span>{name}</span></h1>
<p class="role">{T(d["role"])}</p>
<div class="t-left">
<p class="thesis">{T(d["thesis"])}</p>
{"<p class='lede'>" + T(d["lede"]) + "</p>" if d.get("lede") else ""}
{actions(d["actions"])}
{facts}
</div>
<div class="t-right">{hero}</div>
</div></section>
{opener}
{feats}
{chapters}
{close}
</main>
{colophon}
<script src="{KIT}/monograph.js"></script>
</body>
</html>
"""


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("content")
    ap.add_argument("-o", "--out", required=True)
    a = ap.parse_args()
    d = json.load(open(a.content, encoding="utf-8"))
    open(a.out, "w", encoding="utf-8").write(build(d))
    f, o, i = accent_set(d["accent"])
    print(f"{a.out}  accent {d['accent']} → fill {f} on {o} ({contrast(f, o):.2f}:1) · ink {i} ({contrast(i, PAPER):.2f}:1)")
