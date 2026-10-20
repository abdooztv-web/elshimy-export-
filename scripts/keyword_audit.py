# -*- coding: utf-8 -*-
"""Audit the built site against scripts/keywords_data.py.
Writes docs/keywords.csv and the generated part of docs/keyword-gaps.md.  Run after `python scripts/build.py`:
    python scripts/keyword_audit.py
Matching is on the built HTML: <title>, meta description, <h1>, <h2>, and <main> body text (nav/footer excluded)."""
import csv, os, re, sys
from collections import Counter, defaultdict
from html.parser import HTMLParser
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import keywords_data as K
import content as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")

# ───────────── page paths ─────────────
def path_for(target, lang):
    if isinstance(target, tuple): return f"/{lang}{target[1]}", True
    m = {"home": "/", "products": "/products/", "services": "/sourcing-export/", "freight": "/freight-customs/", "quality": "/quality-food-safety/",
         "markets": "/markets/", "about": "/about/", "contact": "/contact/", "insights": "/insights/", "guide": "/insights/produce-quote-checklist/"}
    if target.startswith("p:"): return f"/{lang}/products/{target[2:]}/", False
    return f"/{lang}{m[target]}", False

# ───────────── parsing ─────────────
class Page(HTMLParser):
    def __init__(s):
        super().__init__(); s.title = s.meta = ""; s.h1 = []; s.h2 = []; s.body = []; s._tag = None; s._main = False; s._skip = 0; s._buf = []
    def handle_starttag(s, t, a):
        a = dict(a)
        if t == "title": s._tag = "title"; s._buf = []
        elif t == "meta" and a.get("name") == "description": s.meta = a.get("content", "")
        elif t in ("h1", "h2"): s._tag = t; s._buf = []
        elif t == "main": s._main = True
        elif t in ("script", "style", "svg", "noscript"): s._skip += 1
    def handle_endtag(s, t):
        if t == "title" and s._tag == "title": s.title = "".join(s._buf).strip(); s._tag = None
        elif t in ("h1", "h2") and s._tag == t: getattr(s, t).append("".join(s._buf).strip()); s._tag = None
        elif t == "main": s._main = False
        elif t in ("script", "style", "svg", "noscript"): s._skip = max(0, s._skip - 1)
    def handle_data(s, d):
        if s._skip: return
        if s._tag: s._buf.append(d)
        if s._main: s.body.append(d)

_cache = {}
def load(path):
    if path in _cache: return _cache[path]
    f = os.path.join(ROOT, path.lstrip("/"), "index.html")
    if not os.path.exists(f): _cache[path] = None; return None
    p = Page(); p.feed(open(f, encoding="utf-8").read()); p.bodytext = " ".join(p.body); _cache[path] = p; return p

# ───────────── normalisation / matching ─────────────
AR_DIAC = re.compile(r"[ً-ْـٰ]")
def norm(text, lang):
    text = text.lower()
    if lang == "ar":
        text = AR_DIAC.sub("", text)
        text = re.sub("[أإآ]", "ا", text).replace("ى", "ي").replace("ة", "ه")
        toks = re.findall(r"[ء-يa-z0-9]+", text)
        out = []
        for t in toks:
            if t.startswith("ال") and len(t) > 3: t = t[2:]
            # light inflection folding so مصري/مصرية/مصريين and مصدر/مصدرين match
            if len(t) > 4 and t.startswith("و"): t = t[1:]  # attached conjunction: وخضروات -> خضروات
            if len(t) > 4 and t.endswith(("ين", "ون")): t = t[:-2]
            elif len(t) > 3 and t.endswith("ه"): t = t[:-1]
            out.append(t)
        return out
    toks = re.findall(r"[a-z0-9]+", text)
    out = []
    for t in toks:
        if len(t) > 3 and t.endswith("ies"): t = t[:-3] + "y"
        elif len(t) > 3 and t.endswith("es") and t[-3] in "sxz": t = t[:-2]
        elif len(t) > 3 and t.endswith("s") and not t.endswith("ss"): t = t[:-1]
        out.append(t)
    return out

STOP_EN = {"for", "from", "of", "in", "to", "and", "the", "a", "an", "how", "what", "is"}
def match(kw_tokens, text_tokens, slack=2):
    """'exact' if tokens appear contiguously, 'near' if in order within a small window, else None."""
    n = len(kw_tokens)
    if n == 0: return None
    for i in range(len(text_tokens)):
        if text_tokens[i] != kw_tokens[0]: continue
        if text_tokens[i:i + n] == kw_tokens: return "exact"
    best = None
    for i in range(len(text_tokens)):
        if text_tokens[i] != kw_tokens[0]: continue
        j, k = i, 0
        while j < len(text_tokens) and j < i + n + slack and k < n:
            if text_tokens[j] == kw_tokens[k]: k += 1
            j += 1
        if k == n: best = "near"; break
    return best

def check(kw, lang, page, brand=False):
    toks = norm(kw, lang)
    if lang == "en": toks = [t for t in toks if t not in STOP_EN]
    found = {}
    fields = {"title": [page.title], "h1": page.h1, "meta": [page.meta], "h2": page.h2, "body": [page.bodytext]}
    for name, texts in fields.items():
        best = None
        for t in texts:
            tt = norm(t, lang)
            if lang == "en": tt = [x for x in tt if x not in STOP_EN]
            m = match(toks, tt)
            if brand and not m and "".join(toks) in "".join(tt): m = "exact"
            if m == "exact": best = "exact"; break
            if m == "near": best = best or "near"
        if best: found[name] = best
    return found

def status_of(found):
    if "title" in found: return "in_title"
    if "h1" in found: return "in_h1"
    if found: return "in_body"
    return "missing"

# ───────────── run ─────────────
def run():
    rows, all_pages = [], [(l, p) for l in ("en", "ar") for p in []]
    results = []
    for kw, lang, intent, cat, slug, target, prio, note in K.ROWS:
        path, is_new = path_for(target, lang)
        url = C.SITE + path
        notes = [note] if note else []
        if is_new:
            status = "missing"
            # closest existing coverage, for context
            best = None
            for alt in ("home", "markets", "freight", "quality", "services", "products"):
                ap, _ = path_for(alt, lang); pg = load(ap)
                if pg:
                    f = check(kw, lang, pg, brand=(intent == K.N))
                    if f: best = (ap, status_of(f), sorted(f)); break
            notes.append("NEW PAGE PROPOSED" + (f"; partial coverage on {best[0]} ({best[1]}: {', '.join(best[2])})" if best else "; not covered anywhere today"))
        else:
            pg = load(path)
            if not pg: status, notes = "missing", notes + ["target page not built"]
            else:
                f = check(kw, lang, pg, brand=(intent == K.N)); status = status_of(f)
                if f: notes.append("found in: " + ", ".join(f"{k}({v})" for k, v in f.items()))
                else:
                    # present on some other page?
                    elsewhere = []
                    for l2, p2 in [(lang, q) for q in ("/", "/products/", "/sourcing-export/", "/freight-customs/", "/quality-food-safety/", "/markets/", "/about/")]:
                        q = load(f"/{lang}{p2}")
                        if q and check(kw, lang, q): elsewhere.append(f"/{lang}{p2}")
                    if elsewhere: notes.append("only on " + ", ".join(elsewhere[:3]))
        results.append(dict(keyword=kw, language=lang, intent=intent, category=cat, product_slug=slug, target_page_url=url, current_status=status,
                            priority=prio, notes="; ".join(notes), search_volume="unvalidated", _new=is_new))
    os.makedirs(DOCS, exist_ok=True)
    cols = ["keyword", "language", "intent", "category", "product_slug", "target_page_url", "current_status", "priority", "notes", "search_volume"]
    with open(os.path.join(DOCS, "keywords.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader(); w.writerows(results)
    return results

def page_table():
    out = []
    for lang in ("en", "ar"):
        paths = ["/", "/products/", "/sourcing-export/", "/freight-customs/", "/quality-food-safety/", "/markets/", "/about/", "/insights/", "/insights/produce-quote-checklist/", "/contact/", "/photo-credits/"] + [f"/products/{p['slug']}/" for p in C.P]
        seen = Counter()
        for p in paths:
            pg = load(f"/{lang}{p}")
            if pg: seen[pg.title] += 1
        for p in paths:
            pg = load(f"/{lang}{p}")
            if not pg: continue
            issues = []
            tl, dl = len(pg.title), len(pg.meta)
            if tl > 62: issues.append(f"title {tl} chars (>62, will truncate)")
            if dl > 160: issues.append(f"description {dl} chars (>160)")
            if dl < 110: issues.append(f"description only {dl} chars")
            if seen[pg.title] > 1: issues.append("duplicate title")
            out.append((lang, f"/{lang}{p}", tl, dl, "; ".join(issues) or "ok", pg.title, pg.meta))
    return out

def main():
    res = run()
    # ── summary
    by = defaultdict(Counter)
    for r in res: by[(r["language"], r["priority"])][r["current_status"]] += 1
    lines = ["# Keyword gaps — elshimytrading.com", "",
             "_Generated by `python scripts/keyword_audit.py` from `scripts/keywords_data.py` against the built HTML. Search volumes are deliberately **unvalidated**: check each row in Google Search Console and Keyword Planner before acting._", "",
             "Status key: **in_title** (strongest) > **in_h1** > **in_body** (meta, H2s or main body) > **missing**. `near` = words present in order but not as an exact phrase.", "",
             "## 1. Coverage summary", "", "| Language | Priority | in_title | in_h1 | in_body | missing |", "|---|---|---|---|---|---|"]
    for lang in ("en", "ar"):
        for pr in ("high", "medium", "low"):
            c = by[(lang, pr)]
            lines.append(f"| {lang} | {pr} | {c['in_title']} | {c['in_h1']} | {c['in_body']} | {c['missing']} |")
    # ── high priority gaps
    def table(rows):
        t = ["| Keyword | Page | Status | Notes |", "|---|---|---|---|"]
        for r in rows: t.append(f"| {r['keyword']} | {r['target_page_url'].replace(C.SITE, '')} | {r['current_status']} | {r['notes'].replace('|', '/')} |")
        return t
    miss = [r for r in res if r["priority"] == "high" and r["current_status"] == "missing" and not r["_new"]]
    weak = [r for r in res if r["priority"] == "high" and r["current_status"] == "in_body" and r["category"] in ("product", "company") and r["intent"] != "navigational"]
    new_ = [r for r in res if r["_new"]]
    lines += ["", "## 2. High-priority keywords that are missing", "", f"{len(miss)} rows.", ""] + table(miss)
    lines += ["", "## 3. High-priority keywords that are weak (in the page body/meta/H2 only, not in title or H1)", "", f"{len(weak)} rows.", ""] + table(weak)
    # ── titles & descriptions
    pt = page_table()
    lines += ["", "## 4. Titles and descriptions", "", "Target: titles ≈ 60 characters, descriptions ≈ 155.", "", "| Page | Title len | Desc len | Issues |", "|---|---|---|---|"]
    for lang, u, tl, dl, iss, *_ in pt:
        if iss != "ok": lines.append(f"| {u} | {tl} | {dl} | {iss} |")
    ok = sum(1 for x in pt if x[4] == "ok")
    lines += ["", f"{ok} of {len(pt)} page titles/descriptions are within range."]
    # patterns: titles starting with the same words
    pat = Counter(re.sub(r"[^|]*\|", "", t[5]).strip() for t in pt if t[0] == "en")
    lines += ["", "Pattern notes:", "- Every product title is `<Name> Export | <descriptor> | EL-SHIMY` — consistent, but the descriptor adds little; replace it with a differentiator (variety, form or market).",
              "- Arabic titles end in `| الشيمي` while English ends in `| EL-SHIMY`: fine for brand consistency, but the Latin brand is what Arabic buyers also type; consider `| EL-SHIMY` in both."]
    # ── new pages
    lines += ["", "## 5. Keywords that need a new page", "", f"{len(new_)} keyword rows point to pages that do not exist yet.", ""]
    grp = defaultdict(list)
    for r in new_: grp[r["target_page_url"].replace(C.SITE, "")].append(r)
    lines += ["| Proposed URL (EN / AR) | Keywords it would serve | Why |", "|---|---|---|"]
    why = {"/markets/gulf-countries/": "Gulf is priority market #1. Today the only coverage is one paragraph on /markets/; country-level queries (Saudi Arabia, UAE) have no landing page.",
           "/insights/import-fresh-produce-from-egypt/": "Highest-volume informational query in the set (how to import). Links naturally to freight, quality, quote form and the existing quote checklist.",
           "/insights/what-is-iqf-frozen-fruit/": "Explains IQF for manufacturers; supports both IQF product pages and the Arabic search 'ما هو IQF'."}
    for path, rs in grp.items():
        base = path[3:]
        ar_slug = {"/markets/gulf-countries/": "/markets/gulf-countries/", "/insights/import-fresh-produce-from-egypt/": "/insights/import-fresh-produce-from-egypt/", "/insights/what-is-iqf-frozen-fruit/": "/insights/what-is-iqf-frozen-fruit/"}[base]
        kws = "; ".join(sorted({f"{r['keyword']} ({r['language']})" for r in rs}))
        lines.append(f"| `/en{base}` and `/ar{ar_slug}` | {kws} | {why[base]} |")
    notes = os.path.join(DOCS, "keyword-gaps-notes.md")  # hand-written sections 6-8 are appended unchanged
    tail = open(notes, encoding="utf-8").read() if os.path.exists(notes) else ""
    open(os.path.join(DOCS, "keyword-gaps.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n" + tail)
    print(f"{len(res)} keywords -> docs/keywords.csv; gaps -> docs/keyword-gaps.md")
    print("page issues:", sum(1 for x in pt if x[4] != "ok"), "of", len(pt))

if __name__ == "__main__":
    main()
