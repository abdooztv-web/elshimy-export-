"""Crop logos and create optimised WebP images. Run once: python scripts/prepare_assets.py"""
import io, urllib.request
from PIL import Image

def crop_logo(src, dst_png, dst_webp=None):
    im = Image.open(src).convert("RGBA")
    # bounding box of non-white / non-transparent content
    bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
    alpha = im.getchannel("A")
    box = alpha.getbbox()
    rgb = Image.alpha_composite(bg, im).convert("L").point(lambda v: 255 if v < 250 else 0)
    box2 = rgb.getbbox()
    b = box2 if (src.endswith("1.png") and box2) else (box or box2)
    pad = 20
    b = (max(b[0]-pad,0), max(b[1]-pad,0), min(b[2]+pad,im.width), min(b[3]+pad,im.height))
    out = im.crop(b)
    out.thumbnail((900, 900))
    out.save(dst_png, optimize=True)
    print(dst_png, out.size)

crop_logo("logo/1.png", "assets/img/logo.png")
crop_logo("logo/3.png", "assets/img/logo-light.png")

# Make the near-white background of the dark logo transparent and cut out the leaf mark
im = Image.open("assets/img/logo.png").convert("RGBA")
px = im.load()
for y in range(im.height):
    for x in range(im.width):
        r, g, b, a = px[x, y]; m = min(r, g, b)
        if m > 235: px[x, y] = (r, g, b, 0)
        elif m > 170: px[x, y] = (r, g, b, int(255 * (235 - m) / 65))
im.save("assets/img/logo.png", optimize=True)
im.crop((0, 0, int(im.width * 0.225), im.height)).save("assets/img/logo-mark.png", optimize=True)

# Mark: leaf symbol only (left part of the logo)




PHOTOS = {  # name: unsplash id (these photos were already used on the previous site)
    "strawberries": "photo-1464965911861-746a04b4bca6",
    "oranges": "photo-1547514701-42782101795e",
    "mangoes": "photo-1601493700631-2b16ec4b4716",
    "watermelon": "photo-1587049352846-4a222e784d38",
    "grapes": "photo-1537640538966-79f369143f8f",
    "mandarins": "photo-1597714026720-8f74c62310ba",
}
for name, pid in PHOTOS.items():
    data = urllib.request.urlopen(f"https://images.unsplash.com/{pid}?w=1600&q=85&auto=format").read()
    im = Image.open(io.BytesIO(data)).convert("RGB")
    for w in (480, 960, 1600):
        if im.width >= w:
            r = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
            r.save(f"assets/img/{name}-{w}.webp", "WEBP", quality=78, method=6)
    print(name, im.size)
