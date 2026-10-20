"""Site QA: broken internal links, titles/descriptions, H1 count, hreflang reciprocity, sitemap coverage, alt text, image files."""
import os, re, sys
from html.parser import HTMLParser
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import content as _C
SITE = _C.SITE

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.links=[]; s.h1=0; s.title=""; s._t=False; s.meta={}; s.canon=None; s.alts={}; s.imgs=[]; s.ids=set(); s.noindex=False
    def handle_starttag(s, t, a):
        a = dict(a)
        if "id" in a: s.ids.add(a["id"])
        if t=="h1": s.h1+=1
        if t=="title": s._t=True
        if t=="meta" and a.get("name")=="description": s.meta["d"]=a.get("content","")
        if t=="meta" and a.get("name")=="robots" and "noindex" in a.get("content",""): s.noindex=True
        if t=="link" and a.get("rel")=="canonical": s.canon=a["href"]
        if t=="link" and a.get("rel")=="alternate": s.alts[a["hreflang"]]=a["href"]
        if t in ("a","link","script") and (a.get("href") or a.get("src")): s.links.append(a.get("href") or a.get("src"))
        if t=="img":
            s.imgs.append(a); s.links.append(a.get("src"))
            if a.get("srcset"): s.links += [x.strip().split()[0] for x in a["srcset"].split(",")]
    def handle_data(s, d):
        if s._t: s.title+=d
    def handle_endtag(s, t):
        if t=="title": s._t=False

def path_to_file(p):
    p = p.split("#")[0].split("?")[0]
    f = os.path.join(ROOT, p.lstrip("/"))
    if p.endswith("/"): f = os.path.join(f, "index.html")
    return f

pages = {}
for dp, dn, fn in os.walk(ROOT):
    if any(x in dp for x in (".git", "scripts", "logo")): continue
    for f in fn:
        if f.endswith(".html"):
            full = os.path.join(dp, f); rel = "/" + os.path.relpath(full, ROOT).replace("\\", "/")
            p = P(); p.feed(open(full, encoding="utf8").read()); pages[rel] = p
errs = []
titles, descs = {}, {}
for rel, p in pages.items():
    url = rel[:-10] if rel.endswith("index.html") else rel
    stub = rel in ("/about.html", "/products.html", "/faqs.html", "/blogs.html", "/404.html")
    for l in p.links:
        if not l or l.startswith(("http", "mailto:", "tel:", "data:")): continue
        f = path_to_file(l)
        if not os.path.exists(f): errs.append(f"{rel}: broken link {l}")
        elif "#" in l and f.endswith(".html"):
            frag = l.split("#")[1]
            tgt = pages.get("/" + os.path.relpath(f, ROOT).replace("\\", "/"))
            if frag and tgt and frag not in tgt.ids: errs.append(f"{rel}: missing anchor {l}")
    if stub: continue
    if p.h1 != 1 and url != "/": errs.append(f"{rel}: {p.h1} h1")
    if not p.title or len(p.title) > 75: errs.append(f"{rel}: title length {len(p.title)}: {p.title}")
    d = p.meta.get("d", "")
    if not d or len(d) > 170: errs.append(f"{rel}: description length {len(d)}")
    titles.setdefault(p.title, []).append(rel); descs.setdefault(d, []).append(rel)
    if p.canon != SITE + url: errs.append(f"{rel}: canonical {p.canon} != {SITE+url}")
    for i in p.imgs:
        if "alt" not in i: errs.append(f"{rel}: img no alt {i.get('src')}")
        if not i.get("width") or not i.get("height"): errs.append(f"{rel}: img no dims {i.get('src')}")
    if url != "/":
        for hl, href in p.alts.items():
            if hl == "x-default": continue
            tp = pages.get(href.replace(SITE, "") + "index.html")
            if not tp: errs.append(f"{rel}: hreflang target missing {href}"); continue
            if tp.alts.get(rel.split("/")[1]) != SITE + url: errs.append(f"{rel}: hreflang not reciprocal with {href}")
for t, r in list(titles.items()) + list(descs.items()):
    if len(r) > 1: errs.append(f"duplicate title/description: {t[:50]} -> {r}")
sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf8").read()
locs = re.findall(r"<loc>([^<]+)</loc>", sm)
for l in locs:
    if not os.path.exists(path_to_file(l.replace(SITE, ""))): errs.append(f"sitemap: missing {l}")
indexable = {(r[:-10] if r.endswith("index.html") else r) for r, p in pages.items() if not p.noindex}
for u in indexable:
    if SITE + u not in locs: errs.append(f"not in sitemap: {u}")
import subprocess
r = subprocess.run(["node", "--check", os.path.join(ROOT, "assets/js/site.js")], capture_output=True, text=True)
if r.returncode: errs.append("site.js syntax error: " + r.stderr.strip()[:200])
print(f"{len(pages)} html files, {len(locs)} sitemap URLs")
print("\n".join(errs) if errs else "ALL CHECKS PASSED")
sys.exit(1 if errs else 0)
