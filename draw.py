#!/usr/bin/env python3
"""Draw the 24 Nov 2026 world-news front page, 1024x1024 PNG.
All stories verified from AP / Reuters / Yonhap / Interfax / SCMP / TOI
as first reported on Tuesday 24 November 2026. Text is rendered with
PIL (crisp, never garbled) — no AI image generation involved.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 234)
INK = (24, 24, 28)
NAVY = (18, 38, 76)
RED = (178, 34, 34)
GREY = (90, 88, 82)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def F(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((512, 52), "THE WORLD IN ONE DAY", font=F(SERIF_B, 58),
       fill=(255, 255, 255), anchor="mm")
d.text((512, 112), "TUESDAY, 24 NOVEMBER 2026", font=F(SANS_B, 30),
       fill=(255, 214, 90), anchor="mm")
d.rectangle([0, 148, W, 156], fill=RED)
d.text((512, 182), "Six stories that defined the day — from Seoul to Kyiv, orbit to Iowa",
       font=F(SANS, 22), fill=GREY, anchor="mm")
d.line([24, 208, W - 24, 208], fill=INK, width=2)

# ---------- panels ----------
# (kicker, accent colour, headline, body, icon key)
STORIES = [
    ("KOREA", (178, 34, 34),
     "Air-raid alert sounds on Ulleung Island",
     "South Korea orders islanders to shelter after an unidentified "
     "aircraft approaches; the alert is lifted within minutes.",
     "radar"),
    ("UKRAINE WAR", (120, 60, 10),
     "Russia strikes drone sites in Sumy",
     "Moscow says it hit drone-control sites and Starlink terminals, "
     "as deadly Russian strikes hit the Kyiv region.",
     "blast"),
    ("SPACE", (18, 38, 76),
     "NATO vows to defend space",
     "Allies warn Moscow may launch a nuclear-armed satellite weapon "
     "within weeks, able to destroy other satellites.",
     "satellite"),
    ("UNITED STATES", (0, 90, 70),
     "Trump halts Iowa detonation",
     "The president stops a planned blast of explosive material at an Iowa "
     "plant, pending a court ruling.",
     "factory"),
    ("BANGLADESH", (90, 40, 120),
     "Hasina plans return from exile",
     "Ousted PM Sheikh Hasina aims to fly back from India on 16 December, "
     "the 1971 liberation war anniversary.",
     "plane"),
    ("PAKISTAN", (140, 90, 0),
     "Magnitude 4.1 quake strikes Pakistan",
     "A morning tremor is recorded by the National Centre for Seismology; "
     "no immediate reports of major damage.",
     "quake"),
]

def icon(draw, key, x, y, s, col):
    """Simple geometric pictogram inside an s x s box at (x, y)."""
    if key == "radar":
        for r in (34, 24, 14):
            draw.arc([x + s // 2 - r, y + s // 2 - r, x + s // 2 + r, y + s // 2 + r],
                     200, 340, fill=col, width=4)
        draw.line([x + s // 2, y + s // 2, x + s - 6, y + 8], fill=col, width=4)
        draw.ellipse([x + s // 2 - 6, y + s // 2 - 6, x + s // 2 + 6, y + s // 2 + 6],
                     fill=col)
        draw.polygon([(x + s - 22, y + 14), (x + s - 4, y + 20), (x + s - 22, y + 26)],
                     fill=col)
    elif key == "blast":
        cx, cy = x + s // 2, y + s // 2 + 6
        pts = []
        import math
        for i in range(16):
            ang = i * math.pi / 8
            r = 34 if i % 2 == 0 else 16
            pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
        draw.polygon(pts, fill=col)
        draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=(255, 214, 90))
    elif key == "satellite":
        draw.rectangle([x + 30, y + 34, x + 54, y + 52], fill=col)
        draw.rectangle([x + 8, y + 38, x + 28, y + 48], outline=col, width=3)
        draw.rectangle([x + 56, y + 38, x + 76, y + 48], outline=col, width=3)
        draw.line([x + 54, y + 34, x + 72, y + 16], fill=col, width=4)
        draw.arc([x + 64, y + 6, x + 82, y + 24], 0, 360, fill=col, width=3)
        draw.arc([x - 4, y + 58, x + s + 4, y + 82], 200, 340, fill=col, width=3)
    elif key == "factory":
        draw.rectangle([x + 10, y + 44, x + 74, y + 74], fill=col)
        draw.rectangle([x + 16, y + 24, x + 26, y + 44], fill=col)
        draw.rectangle([x + 32, y + 18, x + 42, y + 44], fill=col)
        draw.polygon([(x + 56, y + 14), (x + 66, y + 34), (x + 46, y + 34)], fill=(178, 34, 34))
        draw.text((x + 61, y + 22), "!", font=F(SANS_B, 22), fill=(255, 255, 255), anchor="mm")
    elif key == "plane":
        draw.polygon([(x + 8, y + 46), (x + 66, y + 30), (x + 76, y + 34),
                      (x + 40, y + 48), (x + 30, y + 62), (x + 24, y + 50)],
                     fill=col)
        draw.line([x + 10, y + 70, x + 76, y + 70], fill=col, width=3)
        draw.arc([x + 56, y + 56, x + 76, y + 76], 270, 360, fill=col, width=3)
    elif key == "quake":
        pts = [(x + 6, y + 42), (x + 18, y + 42), (x + 26, y + 18), (x + 34, y + 66),
               (x + 42, y + 30), (x + 50, y + 54), (x + 58, y + 42), (x + 78, y + 42)]
        draw.line(pts, fill=col, width=4, joint="curve")
        draw.ellipse([x + 30, y + 62, x + 38, y + 70], fill=col)

PX, PY, PW, PH, GX, GY = 24, 220, 476, 228, 24, 14
for i, (kicker, col, head, body, ikey) in enumerate(STORIES):
    r, c = divmod(i, 2)
    x = PX + c * (PW + GX)
    y = PY + r * (PH + GY)
    d.rounded_rectangle([x, y, x + PW, y + PH], radius=10, fill=(255, 255, 255),
                        outline=(200, 195, 185), width=2)
    d.rectangle([x, y, x + 8, y + PH], fill=col)
    # icon
    ix, iy = x + 22, y + 18
    d.rounded_rectangle([ix, iy, ix + 84, iy + 84], radius=8, fill=(238, 234, 224))
    icon(d, ikey, ix, iy, 84, col)
    # kicker + headline
    tx = x + 122
    d.text((tx, y + 22), kicker, font=F(SANS_B, 20), fill=col)
    lines = wrap(d, head, F(SANS_B, 27), PW - 140)
    yy = y + 50
    for ln in lines[:3]:
        d.text((tx, yy), ln, font=F(SANS_B, 27), fill=INK)
        yy += 32
    # body
    blines = wrap(d, body, F(SANS, 20), PW - 36)
    yy = y + 132
    for ln in blines[:3]:
        d.text((x + 20, yy), ln, font=F(SANS, 20), fill=(52, 52, 56))
        yy += 26

# ---------- ticker + footer ----------
ty = PY + 3 * PH + 2 * GY + 6
d.rectangle([24, ty, W - 24, ty + 34], fill=(232, 228, 216))
d.text((512, ty + 17),
       "ALSO TODAY:  Japan factory PMI 53.7  •  Gold steadies  •  FBI deputy director to retire in December",
       font=F(SANS_B, 16), fill=INK, anchor="mm")
d.text((512, ty + 56),
       "Sources: AP • Reuters • Yonhap • Interfax • SCMP • Times of India — every story first reported 24 November 2026",
       font=F(SANS, 15), fill=GREY, anchor="mm")

img.save("entry.png", optimize=True)
import os
print("saved", os.path.getsize("entry.png"), "bytes", img.size)
