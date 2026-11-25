#!/usr/bin/env python3
"""Builds the 3D Arron logo as SVG (text converted to outlines). Run: python3 _src/logo3d.py"""
import os
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.environ.get("ARRON_FONT", os.path.join(HERE, "Montserrat.ttf"))
OUT = os.path.join(os.path.dirname(HERE), "logo")
os.makedirs(OUT, exist_ok=True)


def load(weight):
    f = TTFont(FONT)
    return instancer.instantiateVariableFont(f, {"wght": weight})


def text_path(font, text, size, x, y, spacing=0.0):
    gs = font.getGlyphSet()
    cmap = font.getBestCmap()
    hmtx = font["hmtx"]
    upm = font["head"].unitsPerEm
    s = size / upm
    d = []
    cx = x
    for ch in text:
        gname = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        gs[gname].draw(TransformPen(pen, (s, 0, 0, -s, cx, y)))
        d.append(pen.getCommands())
        cx += hmtx[gname][0] * s + spacing
    return " ".join(d), cx - spacing - x


# ---- palette (Cowboys-style navy, royal blue and silver; no team marks used)
LIGHT = dict(   # for white / light backgrounds: midnight blue faces, silver edges
    face_top="#1a3f86", face_mid="#0a2255", face_bot="#030e2b",
    ext_a="#a9b5bb", ext_b="#5b6a72",
    silver_a="#f4f7f9", silver_b="#aab6bc", silver_c="#70808a",
    tag_a="#76868e", tag_b="#aab6bc",
    shadow="#020a1c",
    mk=dict(hl="#f2f5f7", hr="#0d2759", ll="#b9c4ca", lr="#041437"),
)
DARK = dict(    # for midnight backgrounds: silver faces, blue-steel edges
    face_top="#ffffff", face_mid="#dbe2e6", face_bot="#98a7af",
    ext_a="#294e96", ext_b="#0a1f4d",
    silver_a="#ffffff", silver_b="#cfd8dd", silver_c="#98a7af",
    tag_a="#c3ccd1", tag_b="#98a7af",
    shadow="#000000",
    mk=dict(hl="#ffffff", hr="#8fa6d6", ll="#d6dde1", lr="#3f66b3"),
)

# mark geometry (300 x 300 box)
P = dict(
    p1=(150, 0), p2=(250, 128), p3=(206, 128), p4=(276, 296), p5=(208, 296),
    p6=(150, 158), p7=(92, 296), p8=(24, 296), p9=(94, 128), p10=(50, 128),
)


def pts(*names):
    return " ".join(f"{P[n][0]},{P[n][1]}" for n in names)


def build(pal, bg=None, name="arron-logo-3d"):
    bold = load(800)
    reg = load(500)
    size, spacing = 218, 7
    ax, ay = 372, 236
    arr_d, arr_w = text_path(bold, "ARRON", size, ax, ay, spacing)
    tag_size = 62
    tag_d, tag_w = text_path(reg, "Ahead of now", tag_size, 0, 0, 1.5)
    # tagline with rules left and right, centred under ARRON
    line_gap = 26
    rule_len = max(60, (arr_w - tag_w - 2 * line_gap) / 2)
    tag_x = ax + rule_len + line_gap
    tag_d, _ = text_path(reg, "Ahead of now", tag_size, tag_x, 322, 1.5)
    rule_y = 322 - tag_size * 0.30
    W = int(ax + arr_w + 60)
    H = 400

    ms = 0.84
    mx, my = 44, 62
    sil_pts = pts("p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10")

    ext_mark = ''.join(
        f'<polygon points="{sil_pts}" fill="{pal["ext_a"] if k > 5 else pal["ext_b"]}" transform="translate({k*1.15:.2f} {k*1.35:.2f})"/>'
        for k in range(14, 0, -1))
    ext_text = ''.join(
        f'<path d="{arr_d}" fill="{pal["ext_a"] if k > 6 else pal["ext_b"]}" transform="translate({k*0.85:.2f} {k*1.0:.2f})"/>'
        for k in range(12, 0, -1))
    mk = pal["mk"]
    bgrect = f'<rect width="{W}" height="{H}" fill="{bg}"/>' if bg else ''
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Arron — Ahead of now">
<defs>
<linearGradient id="face" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{pal['face_top']}"/><stop offset=".5" stop-color="{pal['face_mid']}"/><stop offset="1" stop-color="{pal['face_bot']}"/></linearGradient>
<linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset=".42" stop-color="#fff" stop-opacity=".08"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="silver" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{pal['silver_a']}"/><stop offset=".5" stop-color="{pal['silver_b']}"/><stop offset="1" stop-color="{pal['silver_c']}"/></linearGradient>
<linearGradient id="tag" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{pal['tag_b']}"/><stop offset="1" stop-color="{pal['tag_a']}"/></linearGradient>
<linearGradient id="hl" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{mk['hl']}"/><stop offset="1" stop-color="{mk['ll']}"/></linearGradient>
<linearGradient id="hr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{mk['hr']}"/><stop offset="1" stop-color="{mk['lr']}"/></linearGradient>
<linearGradient id="ll" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{mk['ll']}"/><stop offset="1" stop-color="{mk['hr']}"/></linearGradient>
<linearGradient id="lr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{mk['hr']}"/><stop offset="1" stop-color="{mk['lr']}"/></linearGradient>
<filter id="soft" x="-20%" y="-20%" width="140%" height="160%"><feGaussianBlur stdDeviation="9"/></filter>
<clipPath id="txtclip"><path d="{arr_d}"/></clipPath>
</defs>
{bgrect}
<ellipse cx="{mx+150*ms+10}" cy="{my+300*ms+26}" rx="{150*ms}" ry="13" fill="{pal['shadow']}" opacity=".35" filter="url(#soft)"/>
<ellipse cx="{ax+arr_w/2+8}" cy="{ay+30}" rx="{arr_w/2-20}" ry="8" fill="{pal['shadow']}" opacity=".14" filter="url(#soft)"/>
<g transform="translate({mx} {my}) scale({ms})">
{ext_mark}
<polygon points="{pts('p1','p10','p9','p6')}" fill="url(#hl)"/>
<polygon points="{pts('p1','p2','p3','p6')}" fill="url(#hr)"/>
<polygon points="{pts('p9','p8','p7','p6')}" fill="url(#ll)"/>
<polygon points="{pts('p3','p4','p5','p6')}" fill="url(#lr)"/>
<polyline points="{pts('p8','p9','p10','p1','p2')}" fill="none" stroke="url(#silver)" stroke-width="3.2" stroke-linejoin="round" stroke-linecap="round"/>
<polyline points="{pts('p1','p6')}" fill="none" stroke="#fff" stroke-opacity=".55" stroke-width="2"/>
<polyline points="{pts('p2','p3','p4')}" fill="none" stroke="#fff" stroke-opacity=".18" stroke-width="2" stroke-linejoin="round"/>
</g>
<g>
{ext_text}
<path d="{arr_d}" fill="url(#silver)" transform="translate(-1.7 -1.7)"/>
<path d="{arr_d}" fill="url(#face)"/>
<g clip-path="url(#txtclip)"><rect x="{ax}" y="{ay-160}" width="{arr_w+10}" height="{160}" fill="url(#gloss)"/></g>
</g>
<g>
<rect x="{ax}" y="{rule_y-1.5}" width="{rule_len}" height="3.4" rx="1.7" fill="url(#silver)"/>
<rect x="{ax+arr_w-rule_len}" y="{rule_y-1.5}" width="{rule_len}" height="3.4" rx="1.7" fill="url(#silver)"/>
<path d="{tag_d}" fill="url(#tag)"/>
</g>
</svg>'''
    path = os.path.join(OUT, f"{name}.svg")
    with open(path, "w") as f:
        f.write(svg)
    return path, W, H


if __name__ == "__main__":
    print(build(LIGHT, None, "arron-logo-3d"))
    print(build(DARK, None, "arron-logo-3d-dark"))
    print(build(LIGHT, "#ffffff", "arron-logo-3d-white-bg"))
    print(build(DARK, "#061a42", "arron-logo-3d-navy-bg"))
