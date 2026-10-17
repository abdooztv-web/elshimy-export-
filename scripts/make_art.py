# -*- coding: utf-8 -*-
"""Generates original, license-free brand illustrations into assets/img/ (SVG). Run: python scripts/make_art.py"""
import os
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")
F, F2, G, OR, SAND, WHITE, DEEP = "#0F3D2E", "#17503D", "#5E8B4F", "#E8892B", "#F1ECE0", "#FFFFFF", "#0A2B20"
BLUE = "#3C6E8F"

def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}">'
            f'<title>{title}</title>{body}</svg>')

def container(x, y, w, h, col, ribs=True, reefer=False):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="{col}"/>'
    if ribs:
        n = int(w // 9)
        for i in range(1, n):
            s += f'<rect x="{x + i * 9 - 1}" y="{y + 3}" width="2" height="{h - 6}" fill="#000" opacity=".13"/>'
    s += f'<rect x="{x}" y="{y + h - 3}" width="{w}" height="3" fill="#000" opacity=".25"/>'
    if reefer:
        s += f'<rect x="{x}" y="{y}" width="{w}" height="4" fill="#fff" opacity=".5"/>'
    return s

def wave(y, w, col, amp=8, op=1, step=60):
    d = f"M0 {y}"
    for i in range(0, w + step, step):
        d += f" q {step / 4} {-amp} {step / 2} 0 t {step / 2} 0"
    d += f" V 800 H 0 Z"
    return f'<path d="{d}" fill="{col}" opacity="{op}"/>'

# ───────────── Port scene (hero) ─────────────
def port():
    b = ""
    b += f'<circle cx="930" cy="190" r="92" fill="{OR}" opacity=".92"/><circle cx="930" cy="190" r="130" fill="{OR}" opacity=".12"/>'
    # plane trail
    b += f'<path d="M80 150 C 260 120 420 190 600 110" stroke="#fff" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round" fill="none" opacity=".55"/>'
    b += f'<g transform="translate(600 110) rotate(-18)" fill="#fff"><path d="M0 0 l36 -6 l22 -26 h8 l-8 28 l26 -2 l8 -10 h6 l-4 14 l4 14 h-6 l-8 -10 l-26 -2 l8 28 h-8 l-22 -26 l-36 -6 z"/></g>'
    # sea
    b += wave(560, 1200, "#1E6A50", 8, 1) + wave(600, 1200, "#17503D", 7, 1, 80) + wave(660, 1200, DEEP, 6, 1, 100)
    # crane (left)
    b += f'<g stroke="#F1ECE0" stroke-width="6" stroke-linecap="square" fill="none" opacity=".95"><path d="M90 560 V270 M150 560 V270 M90 270 H150 M60 270 L330 270 M90 270 L40 270"/><path d="M90 340 H150 M90 410 H150 M90 480 H150" stroke-width="3"/><path d="M300 270 V420" stroke-width="3"/></g>'
    b += container(285, 420, 34, 22, OR, ribs=False)
    b += f'<rect x="60" y="552" width="110" height="10" fill="#F1ECE0" opacity=".9"/>'
    # dock stack
    cols = [OR, G, SAND, BLUE, "#C8402B", "#E3C53B"]
    for r in range(3):
        for c in range(3):
            b += container(40 + c * 58, 500 - r * 26 + 26, 54, 24, cols[(r * 3 + c) % 6])
    # ship hull
    b += f'<path d="M330 575 H1130 L1070 640 H400 Z" fill="{DEEP}"/><rect x="345" y="575" width="770" height="9" fill="{OR}"/>'
    # container stacks on ship
    i = 0
    for c in range(11):
        h = 4 if 2 <= c <= 9 else 3
        for r in range(h):
            b += container(360 + c * 62, 549 - r * 26, 58, 24, cols[(c * 2 + r * 3 + i) % 6]); i += 1
    # bridge
    b += f'<rect x="1015" y="470" width="86" height="105" fill="#F1ECE0"/><rect x="1028" y="485" width="60" height="14" fill="{F}" opacity=".85"/><rect x="1028" y="510" width="60" height="14" fill="{F}" opacity=".85"/><rect x="1040" y="450" width="36" height="20" fill="#F1ECE0"/>'
    return svg(1200, 700, b, "Illustration: container ship, port crane and cargo aircraft")

# ───────────── Reefer container (sea) ─────────────
def reefer():
    b = f'<ellipse cx="300" cy="352" rx="250" ry="14" fill="#000" opacity=".25"/>'
    b += f'<rect x="70" y="120" width="360" height="200" rx="6" fill="#F1ECE0"/>'
    for i in range(1, 40): b += f'<rect x="{70 + i * 9}" y="126" width="2.5" height="188" fill="{F}" opacity=".14"/>'
    b += f'<rect x="70" y="120" width="360" height="12" fill="#fff" opacity=".7"/><rect x="70" y="308" width="360" height="12" fill="{F}" opacity=".35"/>'
    b += f'<rect x="430" y="120" width="96" height="200" rx="6" fill="{OR}"/><rect x="444" y="136" width="68" height="68" rx="34" fill="{F}" opacity=".9"/>'
    b += f'<g stroke="#fff" stroke-width="4" stroke-linecap="round" transform="translate(478 170)"><path d="M0 -24V24M-21 -12L21 12M21 -12L-21 12"/></g>'
    b += f'<rect x="446" y="222" width="64" height="12" rx="3" fill="#fff" opacity=".85"/><rect x="446" y="244" width="40" height="8" rx="3" fill="#fff" opacity=".6"/>'
    b += f'<rect x="64" y="318" width="470" height="10" rx="3" fill="{DEEP}"/>'
    b += f'<g transform="translate(150 150)"><rect width="150" height="44" rx="8" fill="{F}" opacity=".92"/><text x="75" y="29" font-family="Manrope,Arial,sans-serif" font-weight="800" font-size="22" fill="#fff" text-anchor="middle">REEFER</text></g>'
    return svg(600, 380, b, "Illustration: refrigerated shipping container")

# ───────────── Cargo aircraft (air) ─────────────
def plane():
    b = f'<circle cx="470" cy="90" r="46" fill="{OR}" opacity=".9"/>'
    for x, y, s in ((60, 80, 1), (360, 200, .8), (120, 250, .7)):
        b += f'<g transform="translate({x} {y}) scale({s})" fill="#fff" opacity=".9"><ellipse cx="40" cy="20" rx="42" ry="14"/><ellipse cx="78" cy="14" rx="30" ry="12"/><ellipse cx="14" cy="22" rx="22" ry="10"/></g>'
    b += f'<g stroke="{F}" stroke-width="3" stroke-linejoin="round">'
    b += f'<path d="M70 170 C 70 140 120 128 190 128 H 430 C 500 128 545 150 565 176 C 545 202 500 214 430 214 H 190 C 120 214 70 202 70 170 Z" fill="#fff"/>'
    b += f'<path d="M70 150 L 36 78 H 84 L 150 134 Z" fill="{OR}"/>'
    b += f'<path d="M250 190 L 190 276 H 250 L 360 200 Z" fill="#E4EEE9"/><path d="M270 138 L 224 80 H 262 L 360 138 Z" fill="#E4EEE9"/>'
    b += f'</g><rect x="200" y="146" width="62" height="54" rx="4" fill="{F}" opacity=".9"/><rect x="205" y="151" width="52" height="44" fill="none" stroke="#fff" stroke-width="2" opacity=".6"/>'
    b += ''.join(f'<circle cx="{480 + i * 20}" cy="160" r="5" fill="{F}"/>' for i in range(0, 2))
    b += f'<path d="M510 166 q 20 -18 50 -6" stroke="{F}" stroke-width="3" fill="none"/>'
    b += f'<rect x="300" y="168" width="60" height="22" rx="3" fill="{OR}"/><rect x="368" y="168" width="40" height="22" rx="3" fill="{G}"/>'
    return svg(600, 320, b, "Illustration: cargo aircraft")

# ───────────── Truck (land) ─────────────
def truck():
    b = f'<path d="M0 300 C 120 250 200 270 300 255 S 480 230 600 262 V 340 H 0Z" fill="{G}" opacity=".35"/>'
    b += f'<rect x="0" y="300" width="600" height="40" fill="{F}" opacity=".9"/><path d="M0 320 H600" stroke="#fff" stroke-width="3" stroke-dasharray="26 22" opacity=".7"/>'
    b += f'<rect x="60" y="120" width="340" height="150" rx="8" fill="#fff" stroke="{F}" stroke-width="3"/>'
    for i in range(1, 17): b += f'<rect x="{60 + i * 20}" y="128" width="2" height="134" fill="{F}" opacity=".1"/>'
    b += f'<rect x="60" y="246" width="340" height="12" fill="{F}" opacity=".18"/>'
    b += f'<g transform="translate(160 160)"><rect width="140" height="44" rx="8" fill="{F}"/><text x="70" y="29" font-family="Manrope,Arial,sans-serif" font-weight="800" font-size="20" fill="#fff" text-anchor="middle">COLD CHAIN</text></g>'
    b += f'<rect x="408" y="134" width="14" height="40" rx="3" fill="{OR}"/>'
    b += f'<path d="M426 170 H 496 L 540 214 V 270 H 426 Z" fill="{OR}" stroke="{F}" stroke-width="3" stroke-linejoin="round"/><path d="M446 184 H 490 L 520 214 H 446 Z" fill="#DCEBF4" stroke="{F}" stroke-width="3" stroke-linejoin="round"/>'
    b += f'<rect x="50" y="268" width="500" height="14" rx="4" fill="{DEEP}"/>'
    for cx in (110, 160, 470, 520):
        b += f'<circle cx="{cx}" cy="296" r="22" fill="{DEEP}"/><circle cx="{cx}" cy="296" r="10" fill="#cfd8d3"/>'
    return svg(600, 340, b, "Illustration: refrigerated truck on a road")

for name, fn in (("ill-port", port), ("ill-reefer", reefer), ("ill-plane", plane), ("ill-truck", truck)):
    with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f: f.write(fn())
    print("wrote", name)
