# -*- coding: utf-8 -*-
"""Static site generator for EL-SHIMY.  Usage: python scripts/build.py   (run from repo root)"""
import json, os, shutil, datetime, html as H
from PIL import Image, ImageDraw, ImageFont
import content as C
import sys
from icons import SPRITE
import visual

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ("en", "ar")
TODAY = datetime.date.today().isoformat()
esc = H.escape

def write(path, text):
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

# ───────────── URL scheme ─────────────
def url(key, lang, slug=None):
    return {
        "home": f"/{lang}/", "products": f"/{lang}/products/", "product": f"/{lang}/products/{slug}/",
        "services": f"/{lang}/sourcing-export/", "freight": f"/{lang}/freight-customs/",
        "quality": f"/{lang}/quality-food-safety/", "about": f"/{lang}/about/", "markets": f"/{lang}/markets/",
        "credits": f"/{lang}/photo-credits/", "insights": f"/{lang}/insights/", "guide": f"/{lang}/insights/{C.GUIDE_SLUG}/", "contact": f"/{lang}/contact/",
    }[key]

def other(lang): return "ar" if lang == "en" else "en"
def abs_url(p): return C.SITE + p
PBY = {p["slug"]: p for p in C.P}
try:
    CREDITS = json.load(open(os.path.join(ROOT, "assets/img/credits.json"), encoding="utf-8"))
except OSError:
    CREDITS = {}

# ───────────── image helpers ─────────────
_dims = {}
def dims(name, w):
    k = (name, w)
    if k not in _dims:
        _dims[k] = Image.open(os.path.join(ROOT, f"assets/img/{name}-{w}.webp")).size
    return _dims[k]

def picture(name, alt, cls="", sizes="100vw", eager=False, max_w=960):
    ws = [w for w in (480, 960, 1600) if os.path.exists(os.path.join(ROOT, f"assets/img/{name}-{w}.webp"))]
    srcset = ", ".join(f"/assets/img/{name}-{w}.webp {w}w" for w in ws)
    base = 960 if 960 in ws else ws[-1]
    w, h = dims(name, base)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img class="{cls}" src="/assets/img/{name}-{base}.webp" srcset="{srcset}" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{esc(alt)}" {load}>')

def tile(p, lang, cls=""):
    n = p["name"][lang]
    return (f'<div class="ph {cls}" style="--accent:{p["accent"]}" role="img" aria-label="{esc(n)}">'
            f'<img class="ph-mark" src="/assets/img/logo-mark.png" alt="" width="64" height="64" loading="lazy"><span>{esc(n)}</span></div>')

def product_media(p, lang, cls="", eager=False, sizes="(min-width:900px) 33vw, 100vw"):
    if p["img"]:
        return picture(p["img"], p["name"][lang], cls="media " + cls, sizes=sizes, eager=eager)
    return tile(p, lang, cls)

# ───────────── layout ─────────────
NAV_ORDER = ["products", "services", "freight", "quality", "markets", "about", "insights"]

def head(lang, title, desc, path, alt_path, extra_ld=(), og_image="/assets/img/og-default.png", noindex=False, hreflang=True):
    ui = C.UI[lang]
    canon = abs_url(path)
    tags = [
        '<meta charset="utf-8">', '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{esc(title)}</title>", f'<meta name="description" content="{esc(desc)}">',
        f'<link rel="canonical" href="{canon}">',
    ]
    if noindex: tags.append('<meta name="robots" content="noindex">')
    if hreflang and alt_path:
        en_p, ar_p = (path, alt_path) if lang == "en" else (alt_path, path)
        tags += [f'<link rel="alternate" hreflang="en" href="{abs_url(en_p)}">',
                 f'<link rel="alternate" hreflang="ar" href="{abs_url(ar_p)}">',
                 f'<link rel="alternate" hreflang="x-default" href="{abs_url("/")}">']
    tags += [
        '<meta property="og:type" content="website">', f'<meta property="og:site_name" content="{C.BRAND}">',
        f'<meta property="og:title" content="{esc(title)}">', f'<meta property="og:description" content="{esc(desc)}">',
        f'<meta property="og:url" content="{canon}">', f'<meta property="og:image" content="{abs_url(og_image)}">',
        '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">',
        f'<meta property="og:locale" content="{"en_US" if lang == "en" else "ar_AR"}">',
        f'<meta property="og:locale:alternate" content="{"ar_AR" if lang == "en" else "en_US"}">',
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="theme-color" content="#0F3D2E">',
        '<link rel="icon" type="image/png" href="/assets/img/logo-mark.png">',
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Manrope:wght@400;500;600;700;800&display=swap">',
        '<link rel="stylesheet" href="/assets/css/site.css">',
    ]
    if C.GSC_TOKEN: tags.append(f'<meta name="google-site-verification" content="{C.GSC_TOKEN}">')
    for ld in extra_ld:
        tags.append('<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>")
    return "\n".join(tags)

def wa_link(lang, text=""):
    if not C.WHATSAPP: return ""
    from urllib.parse import quote
    return f"https://wa.me/{C.WHATSAPP}" + (f"?text={quote(text)}" if text else "")

def header(lang, key, alt_path):
    ui = C.UI[lang]
    cur = ' aria-current="page"'
    items = "".join(
        f'<li><a href="{url(k, lang)}"{cur if k == key else ""}>{ui["nav"][k]}</a></li>' for k in NAV_ORDER)
    return f'''<a class="skip" href="#main">{ui["skip"]}</a>
<header class="site-header" id="top">
 <div class="wrap bar">
  <a class="brand" href="{url("home", lang)}" aria-label="EL-SHIMY"><img src="/assets/img/logo.png" width="180" height="52" alt="EL-SHIMY"></a>
  <nav class="nav" id="nav" aria-label="Main"><ul>{items}</ul></nav>
  <div class="bar-actions">
   <a class="lang" href="{alt_path}" hreflang="{other(lang)}" lang="{other(lang)}" aria-label="{ui["lang_label"]}">{ui["lang_name"]}</a>
   <a class="btn btn-accent btn-sm hide-sm" href="{url("contact", lang)}">{ui["quote"]}</a>
   <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" data-open="{ui["menu"]}" data-close="{ui["close"]}"><span class="bars" aria-hidden="true"></span><span class="sr">{ui["menu"]}</span></button>
  </div>
 </div>
</header>'''

def footer(lang):
    ui = C.UI[lang]
    prods = "".join(f'<li><a href="{url("product", lang, p["slug"])}">{esc(p["name"][lang].split(":")[0])}</a></li>' for p in C.P[:8])
    comp = "".join(f'<li><a href="{url(k, lang)}">{ui["nav"][k]}</a></li>' for k in ("services", "freight", "quality", "markets", "about", "insights"))
    wa = f'<li><a href="{wa_link(lang)}" rel="noopener" target="_blank">{ui["whatsapp"]}</a></li>' if C.WHATSAPP else ""
    return f'''<footer class="site-footer">
 <div class="wrap grid-4">
  <div><img src="/assets/img/logo-light.png" width="170" height="49" alt="EL-SHIMY" loading="lazy"><p class="foot-tag">{ui["footer_tag"]}</p><p class="small">{C.LEGAL[lang]}</p></div>
  <div><h2 class="foot-h">{ui["footer_products"]}</h2><ul>{prods}<li><a href="{url("products", lang)}">{ui["view_all"]}</a></li></ul></div>
  <div><h2 class="foot-h">{ui["footer_company"]}</h2><ul>{comp}</ul></div>
  <div><h2 class="foot-h">{ui["footer_contact"]}</h2><ul><li><a href="{url("contact", lang)}">{ui["quote"]}</a></li><li><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></li>{wa}<li class="small">{C.ADDRESS[lang]}</li></ul></div>
 </div>
 <div class="wrap foot-bottom"><p class="small">© {datetime.date.today().year} {C.LEGAL[lang]}. {ui["rights"]}</p><p class="small">{ui["img_note"]} <a href="{url("credits", lang)}">{ui["credits"]}</a></p></div>
</footer>'''

def crumbs(lang, trail):
    """trail: list of (label, path); last has path None."""
    ui = C.UI[lang]
    items = [(ui["home"], url("home", lang))] + trail
    lis = []
    for i, (lbl, pth) in enumerate(items):
        if pth and i < len(items) - 1: lis.append(f'<li><a href="{pth}">{esc(lbl)}</a></li>')
        else: lis.append(f'<li aria-current="page">{esc(lbl)}</li>')
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": lbl, **({"item": abs_url(pth)} if pth else {})}
        for i, (lbl, pth) in enumerate(items[:-1] + [(items[-1][0], None)])]}
    # last item: Google allows omitting `item` for the current page
    return f'<nav class="crumbs" aria-label="{ui["breadcrumb"]}"><ol>{"".join(lis)}</ol></nav>', ld

def page(lang, key, path, alt_path, title, desc, body, ld=(), slug=None, og_image="/assets/img/og-default.png"):
    dir_ = "rtl" if lang == "ar" else "ltr"
    return f'''<!doctype html>
<html lang="{lang}" dir="{dir_}">
<head>
{head(lang, title, desc, path, alt_path, ld, og_image)}
</head>
<body class="lang-{lang}">
{SPRITE}
{header(lang, key, alt_path)}
<main id="main">
{body}
</main>
{footer(lang)}
<script src="/assets/js/site.js" defer></script>
</body>
</html>
'''

def cta_band(lang, text=None, sub=None, product=None):
    ui = C.UI[lang]; h = C.HOME[lang]
    href = url("contact", lang) + (f"?product={product}" if product else "")
    wa = f'<a class="btn btn-ghost" href="{wa_link(lang)}" target="_blank" rel="noopener">{ui["whatsapp"]}</a>' if C.WHATSAPP else ""
    return f'''<section class="cta-band"><div class="wrap cta-in reveal"><div><h2>{text or h["cta_h"]}</h2><p>{sub or h["cta_p"]}</p></div><div class="cta-actions"><a class="btn btn-accent" href="{href}">{ui["quote"]}</a>{wa}</div></div></section>'''

def card(p, lang):
    ui = C.UI[lang]
    form_label = ui["frozen"] if p["form"] == "frozen" else ui["fresh"]
    u = url("product", lang, p["slug"])
    return f'''<article class="card reveal" data-cat="{p["cat"]}" data-form="{p["form"]}" data-name="{esc((p["name"]["en"] + " " + p["name"]["ar"]).lower())}">
 <div class="card-media">{product_media(p, lang)}<span class="badge badge-{p["form"]}">{form_label}</span></div>
 <div class="card-body"><h3><a class="stretch" href="{u}">{esc(p["name"][lang])}</a></h3><p>{esc(p["tag"][lang])}</p>
 <a class="quote-link" href="{url("contact", lang)}?product={p["slug"]}">{ui["quote"]} →</a></div>
</article>'''

# ───────────── pages ─────────────
def build_home(lang):
    ui = C.UI[lang]; d = C.PAGES["home"][lang]; h = C.HOME[lang]; a = url("home", other(lang))
    featured = [PBY[s] for s in ("egyptian-oranges", "egyptian-potatoes", "yellow-onions", "grapes", "strawberries", "iqf-strawberries")]
    cat_cards = ""
    for cat, key in (("veg", "veg"), ("fruit", "fruit"), ("frozen", "frozen_cat")):
        names = [p["name"][lang].split(":")[0] for p in C.P if p["cat"] == cat]
        cat_cards += f'<a class="cat reveal" href="{url("products", lang)}?cat={cat}"><span class="cat-n">{ui[key]}</span><span class="cat-l">{esc(" · ".join(names[:5]))}{"…" if len(names) > 5 else ""}</span><span class="cat-go" aria-hidden="true">→</span></a>'
    how = "".join(f'<li class="reveal"><span class="step">{i + 1}</span><h3>{t}</h3><p>{s}</p></li>' for i, (t, s) in enumerate(h["how"]))
    svc = "".join(f'<a class="svc reveal" href="{url(k, lang)}"><h3>{t}</h3><p>{s}</p><span class="more">{ui["learn_more"]} →</span></a>' for k, t, s in h["svc"])
    strip = "".join(f"<li>{s}</li>" for s in h["strip"])
    wa = f'<a class="btn btn-ghost-light" href="{wa_link(lang)}" target="_blank" rel="noopener">{ui["whatsapp"]}</a>' if C.WHATSAPP else ""
    hero_alt = {"en": "Fresh strawberries (illustrative stock photo)", "ar": "فراولة طازجة (صورة توضيحية)"}[lang]
    body = f'''<section class="hero"><div class="wrap hero-grid">
 <div class="hero-copy"><p class="eyebrow">{C.LEGAL[lang]}</p><h1>{d["h1"]}</h1><p class="lead">{d["lead"]}</p>
 <div class="hero-actions"><a class="btn btn-accent" href="{url("contact", lang)}">{ui["quote"]}</a><a class="btn btn-ghost-light" href="{url("products", lang)}">{ui["view_all"]}</a>{wa}</div></div>
 <figure class="hero-fig">{picture("strawberries", hero_alt, cls="hero-img", sizes="(min-width:900px) 50vw, 100vw", eager=True)}<figcaption>{ {"en": "Illustrative stock photo", "ar": "صورة توضيحية"}[lang] }</figcaption></figure>
</div></section>
<section class="strip"><ul class="wrap">{strip}</ul></section>
<section class="section"><div class="wrap"><div class="sec-head reveal"><h2>{h["cats_h"]}</h2><p>{h["cats_lead"]}</p></div><div class="cats">{cat_cards}</div></div></section>
<section class="section alt"><div class="wrap"><div class="sec-head reveal"><h2>{h["feat_h"]}</h2></div><div class="cards">{"".join(card(p, lang) for p in featured)}</div><p class="center"><a class="btn btn-primary" href="{url("products", lang)}">{ui["view_all"]}</a></p></div></section>
<section class="section"><div class="wrap"><div class="sec-head reveal"><h2>{h["how_h"]}</h2><p>{h["model"]}</p></div><ol class="steps">{how}</ol></div></section>
<section class="section alt"><div class="wrap"><div class="sec-head reveal"><h2>{h["svc_h"]}</h2><p>{h["svc_lead"]}</p></div><div class="svcs">{svc}</div></div></section>
{cta_band(lang)}'''
    org = {"@context": "https://schema.org", "@type": "Organization", "name": C.LEGAL["en"], "alternateName": C.BRAND,
           "url": abs_url("/"), "logo": abs_url("/assets/img/logo.png"), "foundingDate": "2016",
           "email": C.EMAIL, "address": {"@type": "PostalAddress", "streetAddress": "Office 3, Mall 11, Beverly Hills", "addressLocality": "Giza", "addressCountry": "EG"},
           "description": C.PAGES["home"]["en"]["lead"]}
    return page(lang, "home", url("home", lang), a, d["title"], d["meta"], body, ld=[org])

def build_products_index(lang):
    ui = C.UI[lang]; d = C.PAGES["products"][lang]; a = url("products", other(lang))
    bc, ld = crumbs(lang, [(ui["nav"]["products"], None)])
    chips = "".join(f'<button type="button" class="chip" data-filter-cat="{k}" aria-pressed="false">{ui[v]}</button>' for k, v in (("veg", "veg"), ("fruit", "fruit"), ("frozen", "frozen_cat")))
    forms = "".join(f'<button type="button" class="chip" data-filter-form="{k}" aria-pressed="false">{ui[v]}</button>' for k, v in (("fresh", "fresh"), ("frozen", "frozen")))
    groups = ""
    for cat, key in (("veg", "veg"), ("fruit", "fruit"), ("frozen", "frozen_cat")):
        groups += f'<section class="group" id="{cat}" data-group="{cat}"><h2>{ui[key]}</h2><div class="cards">{"".join(card(p, lang) for p in C.P if p["cat"] == cat)}</div></section>'
    body = f'''{visual.build_products_hero(lang, bc, d["h1"], d["lead"])}
<section class="section"><div class="wrap">
<div class="filters" role="group" aria-label="{ui["filters"]}">
 <div class="chips"><button type="button" class="chip" data-filter-cat="all" aria-pressed="true">{ui["all"]}</button>{chips}</div>
 <div class="chips"><button type="button" class="chip" data-filter-form="all" aria-pressed="true">{ui["fresh"]} + {ui["frozen"]}</button>{forms}</div>
 <label class="search"><span class="sr">{ui["search"]}</span><input type="search" id="p-search" placeholder="{ui["search"]}" autocomplete="off"></label>
</div>
<p class="empty" id="p-empty" hidden>{ui["no_results"]}</p>
<div id="p-groups">{groups}</div></div></section>
{cta_band(lang)}'''
    return page(lang, "products", url("products", lang), a, d["title"], d["meta"], body, ld=[ld])

def build_product(lang, p):
    ui = C.UI[lang]; a = url("product", other(lang), p["slug"]); path = url("product", lang, p["slug"])
    cat_key = {"veg": "veg", "fruit": "fruit", "frozen": "frozen_cat"}[p["cat"]]
    bc, ld = crumbs(lang, [(ui["nav"]["products"], url("products", lang)), (p["name"][lang], None)])
    form_label = ui["frozen"] if p["form"] == "frozen" else ui["fresh"]
    caption = ""
    if p["img"]:
        cr = CREDITS.get(p["img"])
        if cr:
            lead = {"en": "Illustrative photo", "ar": "صورة توضيحية"}[lang]
            caption = f'<figcaption>{lead}: {esc(cr["artist"])}, <a href="{cr["license_url"] or cr["source"]}" rel="noopener">{esc(cr["license"])}</a> · <a href="{url("credits", lang)}">{C.UI[lang]["credits"]}</a></figcaption>'
        else:
            caption = f'<figcaption>{ {"en": "Illustrative stock photo", "ar": "صورة توضيحية"}[lang] }</figcaption>'
    media = f'<figure class="p-fig">{product_media(p, lang, eager=True, sizes="(min-width:900px) 45vw, 100vw")}{caption}</figure>'
    det = ""
    for i, (k, lbl) in enumerate((("varieties", "varieties"), ("sizes", "sizes"), ("packing", "packaging"), ("storage", "storage"), ("docs", "docs"))):
        det += f'<details{" open" if i == 0 else ""}><summary>{ui[lbl]}</summary><p>{esc(p[k][lang])}</p></details>'
    rel = [q for q in C.P if q["cat"] == p["cat"] and q["slug"] != p["slug"]][:3]
    if len(rel) < 3: rel += [q for q in C.P if q["cat"] != p["cat"] and q not in rel][: 3 - len(rel)]
    wa = f'<a class="btn btn-ghost" href="{wa_link(lang, ui["request_quote_for"] + " " + p["name"][lang])}" target="_blank" rel="noopener">{ui["whatsapp"]}</a>' if C.WHATSAPP else ""
    body = f'''<section class="page-head p-head"><div class="wrap">{bc}
<div class="p-grid"><div><h1>{esc(p["name"][lang])}</h1><p class="lead">{esc(p["intro"][lang])}</p>
<div class="hero-actions"><a class="btn btn-accent" href="{url("contact", lang)}?product={p["slug"]}">{ui["request_quote_for"]} {esc(p["name"][lang].split(":")[0])}</a>{wa}</div></div>{media}</div></div></section>
<section class="section"><div class="wrap p-body"><div>
<h2>{ui["spec_title"]}</h2>
<dl class="facts"><div><dt>{ui["category"]}</dt><dd>{ui[cat_key]}</dd></div><div><dt>{ui["type"]}</dt><dd>{form_label}</dd></div><div><dt>{ui["season"]}</dt><dd>{esc(p["season"][lang])}</dd></div></dl>
<p class="note">{ui["season_note"]}</p>
<h2>{ui["details_title"]}</h2><div class="acc">{det}</div>
<p class="note">{ui["spec_note"]}</p></div>
<aside class="side"><h2>{ui["quote"]}</h2><p>{C.HOME[lang]["cta_p"]}</p><a class="btn btn-primary btn-block" href="{url("contact", lang)}?product={p["slug"]}">{ui["quote"]}</a></aside></div></section>
<section class="section alt"><div class="wrap"><div class="sec-head"><h2>{ui["related"]}</h2></div><div class="cards">{"".join(card(q, lang) for q in rel)}</div></div></section>'''
    return page(lang, "products", path, a, p["title"][lang], p["meta"][lang], body, ld=[ld])

def build_static(lang, key):
    ui = C.UI[lang]; d = C.PAGES[key][lang]; a = url(key, other(lang)); path = url(key, lang)
    trail = [(ui["nav"][key] if key in ui["nav"] else d["h1"], None)]
    if key == "guide": trail = [(ui["nav"]["insights"], url("insights", lang)), (d["h1"], None)]
    bc, ld = crumbs(lang, trail)
    secs = ""
    for h2, paras in d.get("sections", []):
        inner = "".join(x if x.startswith("<") else f"<p>{x}</p>" for x in paras)
        secs += f'<section class="prose-sec reveal"><h2>{h2}</h2>{inner}</section>'
    extra = ""
    if key == "about" and (C.SHOW_VOLUME):
        extra = ""
    if key == "quality" and C.SHOW_ISO:
        extra = '<section class="prose-sec"><h2>ISO 22000</h2><p>ISO 22000 certified.</p></section>'
    if key == "insights":
        g = C.PAGES["guide"][lang]
        secs = f'<div class="cards cards-2"><article class="card reveal"><div class="card-body"><h3><a class="stretch" href="{url("guide", lang)}">{g["h1"]}</a></h3><p>{g["lead"]}</p><span class="quote-link">{ui["learn_more"]} →</span></div></article></div>'
    body = f'''<section class="page-head"><div class="wrap">{bc}<h1>{d["h1"]}</h1><p class="lead">{d["lead"]}</p></div></section>
<section class="section"><div class="wrap prose">{secs}{extra}</div></section>
{cta_band(lang)}'''
    return page(lang, key if key != "guide" else "insights", path, a, d["title"], d["meta"], body, ld=[ld])

def build_credits(lang):
    ui = C.UI[lang]; d = C.CREDITS[lang]; a = url("credits", other(lang))
    bc, ld = crumbs(lang, [(d["h1"], None)])
    rows = ""
    for p in C.P:
        cr = CREDITS.get(p["img"] or "")
        if not cr: continue
        rows += (f'<tr><th scope="row"><a href="{url("product", lang, p["slug"])}">{esc(p["name"][lang].split(":")[0])}</a></th><td>{esc(cr["artist"])}</td>'
                 f'<td><a href="{cr["license_url"] or cr["source"]}" rel="noopener">{esc(cr["license"])}</a></td><td><a href="{cr["source"]}" rel="noopener">{d["view"]}</a></td></tr>')
    head_ = "".join(f"<th scope='col'>{c_}</th>" for c_ in d["cols"])
    body = f'''{visual.hero_lite(lang, bc, d["h1"], d["lead"], cls="hero-compact")}
<section class="section"><div class="wrap prose"><div class="matrix-wrap" tabindex="0" role="region" aria-label="{d["h1"]}"><table class="cmp"><thead><tr>{head_}</tr></thead><tbody>{rows}</tbody></table></div><p class="note">{d["unsplash"]}</p></div></section>'''
    return page(lang, "credits", url("credits", lang), a, d["title"], d["meta"], body, ld=[ld])

def build_contact(lang):
    ui = C.UI[lang]; f = C.FORM[lang]; d = C.PAGES["contact"][lang]; a = url("contact", other(lang))
    bc, ld = crumbs(lang, [(d["h1"], None)])
    opts = "".join(f'<option value="{p["slug"]}">{esc(p["name"][lang].split(":")[0])}</option>' for p in C.P)
    def field(i, label, typ="text", req=True, ac=""):
        r = f' required aria-required="true"' if req else ""
        mark = f' <span class="req" aria-hidden="true">*</span>' if req else ""
        acx = f' autocomplete="{ac}"' if ac else ""
        return f'<div class="field"><label for="{i}">{label}{mark}</label><input id="{i}" name="{i}" type="{typ}"{r}{acx} aria-describedby="{i}-err"><p class="err" id="{i}-err" hidden></p></div>'
    wa = f'<p><a class="btn btn-ghost" href="{wa_link(lang)}" target="_blank" rel="noopener">{ui["whatsapp"]}</a></p>' if C.WHATSAPP else ""
    msgs = json.dumps({"required": f["e_required"], "email": f["e_email"], "summary": f["summary"], "sending": f["sending"],
                       "ok_endpoint": f["ok_endpoint"], "ok_mailto": f["ok_mailto"], "fail": f["fail"], "email_addr": C.EMAIL}, ensure_ascii=False)
    body = f'''{visual.hero_lite(lang, bc, d["h1"], d["lead"], cls="hero-compact")}
<section class="section"><div class="wrap contact-grid">
<form id="quote-form" class="form" novalidate data-topics='{esc(json.dumps(visual.TOPICS[lang], ensure_ascii=False), quote=True)}' data-tpl='{esc(json.dumps(visual.V[lang]["guide"]["tpl"], ensure_ascii=False), quote=True)}' data-endpoint="{C.FORM_ENDPOINT}" data-email="{C.EMAIL}" data-lang="{lang}" data-msgs='{esc(msgs, quote=True)}'>
 <div id="form-summary" class="summary" role="alert" tabindex="-1" hidden></div>
 <div class="row">{field("name", f["name"], ac="name")}{field("company", f["company"], ac="organization")}</div>
 <div class="row">{field("email", f["email"], "email", ac="email")}{field("phone", f["phone"], "tel", req=False, ac="tel")}</div>
 <div class="row">{field("country", f["country"], ac="country-name")}
  <div class="field"><label for="product">{f["product"]} <span class="req" aria-hidden="true">*</span></label><select id="product" name="product" required aria-required="true" aria-describedby="product-err"><option value="">{f["choose"]}</option>{opts}<option value="other">{f["other"]}</option></select><p class="err" id="product-err" hidden></p></div></div>
 {field("qty", f["qty"], req=False)}
 <div class="field"><label for="message">{f["msg"]}</label><textarea id="message" name="message" rows="5" placeholder="{f["msg_ph"]}"></textarea></div>
 <div class="hp" aria-hidden="true"><label>Website<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
 <p class="small">{f["privacy"]}</p>
 <button class="btn btn-primary" type="submit">{f["send"]}</button>
 <div id="form-status" class="status" role="status" aria-live="polite"></div>
</form>
<aside class="side"><h2>{f["direct"]}</h2><p><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>{wa}<p class="small"><strong>{f["address"]}:</strong> {C.ADDRESS[lang]}</p></aside>
</div></section>'''
    return page(lang, "contact", url("contact", lang), a, d["title"], d["meta"], body, ld=[ld])

def build_404():
    out = ""
    for lang in LANGS:
        n = C.NOTFOUND[lang]
        links = "".join(f'<li><a href="{url(k, lang)}">{C.UI[lang]["nav"][k]}</a></li>' for k in ("products", "contact", "services"))
        out += f'<section lang="{lang}" dir="{"rtl" if lang == "ar" else "ltr"}" class="nf"><h2>{n["h1"]}</h2><p>{n["lead"]}</p><p><a class="btn btn-primary" href="{url("home", lang)}">{C.UI[lang]["home"]}</a></p><ul class="nf-links">{links}</ul></section>'
    return f'''<!doctype html>
<html lang="en">
<head>
{head("en", "Page not found | EL-SHIMY · الصفحة غير موجودة", "Page not found.", "/404.html", None, noindex=True, hreflang=False)}
</head>
<body class="lang-en">
<header class="site-header"><div class="wrap bar"><a class="brand" href="/"><img src="/assets/img/logo.png" width="180" height="52" alt="EL-SHIMY"></a></div></header>
<main id="main" class="wrap nf-wrap"><h1>404</h1>{out}</main>
</body></html>
'''

def build_root():
    en, ar = C.PAGES["home"]["en"], C.PAGES["home"]["ar"]
    title = "EL-SHIMY | Egyptian Fruit & Vegetable Exporter · مُصدّر فاكهة وخضروات مصرية"
    desc = "EL-SHIMY for Trading & Agencies. Choose your language: English or العربية."
    org_ld = {"@context": "https://schema.org", "@type": "Organization", "name": C.LEGAL["en"], "url": abs_url("/"), "logo": abs_url("/assets/img/logo.png")}
    h = head("en", title, desc, "/", "/ar/", [org_ld])
    h = h.replace(f'<link rel="alternate" hreflang="en" href="{abs_url("/")}">', f'<link rel="alternate" hreflang="en" href="{abs_url("/en/")}">')
    return f'''<!doctype html>
<html lang="en">
<head>
{h}
</head>
<body class="lang-en chooser">
<main id="main" class="chooser-in">
 <img src="/assets/img/logo.png" width="240" height="69" alt="EL-SHIMY">
 <h1 class="sr">EL-SHIMY</h1>
 <p class="lead">Egyptian Products. Global Markets.</p>
 <p class="lead" lang="ar" dir="rtl">منتجات مصرية. أسواق عالمية.</p>
 <div class="hero-actions"><a class="btn btn-primary" href="/en/" hreflang="en" lang="en">English</a><a class="btn btn-primary" href="/ar/" hreflang="ar" lang="ar">العربية</a></div>
</main>
</body></html>
'''

def build_redirect(target, label):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Moved | EL-SHIMY</title>
<meta name="robots" content="noindex"><link rel="canonical" href="{abs_url(target)}">
<meta http-equiv="refresh" content="0; url={target}"></head>
<body><p>This page has moved to <a href="{target}">{label}</a>.</p></body></html>
'''

def sitemap(entries):
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for loc, alts in entries:
        out.append(f"<url><loc>{abs_url(loc)}</loc><lastmod>{TODAY}</lastmod>")
        for hl, href in alts:
            out.append(f'<xhtml:link rel="alternate" hreflang="{hl}" href="{abs_url(href)}"/>')
        out.append("</url>")
    out.append("</urlset>")
    return "\n".join(out)

def og_image():
    W, Hh = 1200, 630
    im = Image.new("RGB", (W, Hh), "#0F3D2E")
    logo = Image.open(os.path.join(ROOT, "assets/img/logo-light.png")).convert("RGBA")
    logo.thumbnail((760, 300)); im.paste(logo, ((W - logo.width) // 2, 170), logo)
    d = ImageDraw.Draw(im)
    try: f = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 40)
    except Exception: f = ImageFont.load_default()
    t = "Egyptian Products. Global Markets."
    tw = d.textlength(t, font=f); d.text(((W - tw) / 2, 400), t, fill="#F2B56B", font=f)
    im.save(os.path.join(ROOT, "assets/img/og-default.png"), optimize=True)

def main():
    visual.init(sys.modules[__name__])
    og_image()
    # clean generated dirs
    for d_ in ("en", "ar"): shutil.rmtree(os.path.join(ROOT, d_), ignore_errors=True)
    entries = [("/", [("en", "/en/"), ("ar", "/ar/"), ("x-default", "/")])]
    def reg(key, slug=None):
        entries.append((url(key, "en", slug), [("en", url(key, "en", slug)), ("ar", url(key, "ar", slug)), ("x-default", "/")]))
        entries.append((url(key, "ar", slug), [("en", url(key, "en", slug)), ("ar", url(key, "ar", slug)), ("x-default", "/")]))
    for lang in LANGS:
        write(url("home", lang) + "index.html", visual.build_home(lang))
        write(url("products", lang) + "index.html", build_products_index(lang))
        for p in C.P: write(url("product", lang, p["slug"]) + "index.html", build_product(lang, p))
        for k, fn in (("services", visual.build_services), ("freight", visual.build_freight), ("quality", visual.build_quality), ("about", visual.build_about),
                      ("markets", visual.build_markets), ("insights", visual.build_insights), ("guide", visual.build_guide)):
            write(url(k, lang) + "index.html", fn(lang))
        write(url("contact", lang) + "index.html", build_contact(lang))
        write(url("credits", lang) + "index.html", build_credits(lang))
    for k in ("home", "products", "services", "freight", "quality", "about", "markets", "insights", "guide", "contact", "credits"): reg(k)
    for p in C.P: reg("product", p["slug"])
    # Fix home x-default: both language homes point x-default to the chooser at "/"
    write("index.html", build_root())
    write("404.html", build_404())
    # Legacy URL stubs (host-agnostic) + host redirect configs
    legacy = {"about.html": "/en/about/", "products.html": "/en/products/", "faqs.html": "/en/insights/", "blogs.html": "/en/insights/"}
    for f, t in legacy.items(): write(f, build_redirect(t, t))
    write("sitemap.xml", sitemap(entries))
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {abs_url('/sitemap.xml')}\n")
    write("_redirects", "".join(f"/{f}  {t}  301\n" for f, t in legacy.items()))
    write("vercel.json", json.dumps({"trailingSlash": True, "redirects": [{"source": f"/{f}", "destination": t, "permanent": True} for f, t in legacy.items()]}, indent=2) + "\n")
    print("pages:", len(entries), "URLs in sitemap")

if __name__ == "__main__":
    main()
