# -*- coding: utf-8 -*-
"""Download product photos from Wikimedia Commons (CC0 / public domain / CC BY / CC BY-SA), resize to WebP
and write assets/img/credits.json for attribution. Run once: python scripts/fetch_photos.py"""
import io, json, os, re, html, time, urllib.parse, urllib.request
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "elshimy-site/1.0 (abdooztv@gmail.com)"}
PHOTOS = {  # product image name -> Commons file title (manually checked to show the named product)
    "potatoes": "File:Au marché - pommes de terre.JPG",
    "strawberries-fresh": "File:BERRY...BERRY... - Flickr - Have a nice day ^.jpg",
    "iqf-strawberries": "File:Frozen goodness (6386754543).jpg",
    "yellow-onions": "File:500px photo (39214994).jpeg",
    "red-onions": "File:9892Baliuag, Bulacan during Pandemic Lockdown 02.jpg",
    "tomatoes": "File:AgroFidanishtja Havolli tomato's.jpg",
    "lemons": "File:Citrus limon (Rutaceae).jpg",
    "pomegranates": "File:Granadas - panoramio.jpg",
    "dates": "File:Date palm - Anduhjerd, Shahdad, Kerman.jpg",
    "guava": "File:COMMON GUAVA.jpg",
    "pears": "File:Corbeille de poires-1-cliche Jean Weber (23048297373).jpg",
    "stone-fruits": "File:Apricots 2 - Farmer's Market at the Ferry Building - San Francisco, CA - DSC03603.JPG",
    "prickly-pear": "File:Prickly Pear Fruit (50618126823).jpg",
    "iqf-berries": "File:Frozen Raspberries.jpg",
    "vegetables": "File:A selection of vegetables 01.jpg",  # home page category tile
}
def get(u):
    for i in range(5):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read()
        except Exception: time.sleep(3 * (i + 1))
    raise RuntimeError(u)
import sys
only = sys.argv[1:]  # optional: fetch only these names (existing credits are kept)
cpath = os.path.join(ROOT, "assets/img/credits.json")
credits = json.load(open(cpath, encoding="utf-8")) if only and os.path.exists(cpath) else {}
for name, title in PHOTOS.items():
    if only and name not in only: continue
    q = urllib.parse.urlencode({"action": "query", "titles": title, "prop": "imageinfo", "iiprop": "url|extmetadata", "iiurlwidth": 1600, "format": "json"})
    p = next(iter(json.loads(get("https://commons.wikimedia.org/w/api.php?" + q))["query"]["pages"].values()))["imageinfo"][0]
    m = p["extmetadata"]
    artist = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html.unescape(m.get("Artist", {}).get("value", "")))).strip()
    credits[name] = {"title": title[5:], "artist": artist or "Unknown", "license": m["LicenseShortName"]["value"],
                     "license_url": m.get("LicenseUrl", {}).get("value", ""), "source": p["descriptionurl"]}
    im = Image.open(io.BytesIO(get(p["thumburl"]))).convert("RGB")
    for w in (480, 960, 1600):
        if im.width >= w:
            im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(os.path.join(ROOT, f"assets/img/{name}-{w}.webp"), "WEBP", quality=78, method=6)
    print(name, im.size, credits[name]["license"])
json.dump(credits, open(os.path.join(ROOT, "assets/img/credits.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
