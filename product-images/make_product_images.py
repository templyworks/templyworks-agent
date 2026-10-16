"""Templyworks product images (2048x2048), 4 per template, built from real screenshots."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(HERE, "shots")
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)
S = 2048
BG = (6, 18, 16)
BRAND = (61, 214, 127)
TEXT = (240, 246, 242)
MUTED = (150, 176, 163)
CARD = (13, 31, 27)
LINE = (36, 74, 62)
F = "/usr/share/fonts/opentype/inter/"


def font(w, size):
    return ImageFont.truetype(F + {"b": "InterDisplay-Bold.otf", "sb": "InterDisplay-SemiBold.otf",
                                   "m": "Inter-Medium.otf", "r": "Inter-Regular.otf",
                                   "xb": "InterDisplay-ExtraBold.otf"}[w], size)


EMOJI = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", 109)


def emoji(ch, size):
    im = Image.new("RGBA", (160, 160), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((10, 10), ch, font=EMOJI, embedded_color=True)
    im = im.crop(im.getbbox())
    return im.resize((size, int(size * im.height / im.width)), Image.LANCZOS)


def bg(accent):
    img = Image.new("RGB", (S, S), BG)
    g = Image.new("RGB", (S, S), BG)
    d = ImageDraw.Draw(g)
    a = accent
    d.ellipse((1100, -500, 2500, 700), fill=(16, 64, 44))
    d.ellipse((-400, 900, 1200, 2400), fill=tuple(int(c * .22) for c in a))
    img = Image.blend(img, g.filter(ImageFilter.GaussianBlur(220)), 1.0)
    d = ImageDraw.Draw(img)
    for x in range(0, S, 40):
        for y in range(0, S, 40):
            d.point((x, y), fill=(20, 42, 35))
    return img


def logo(d, x, y):
    d.text((x, y), "T", font=font("xb", 64), fill=TEXT)
    d.text((x + 34, y), "W", font=font("xb", 64), fill=BRAND)
    d.text((x + 120, y), "Temply", font=font("b", 60), fill=TEXT)
    w = d.textlength("Temply", font=font("b", 60))
    d.text((x + 120 + w, y), "works", font=font("b", 60), fill=BRAND)


def pill(d, x_right, y, text, accent):
    f = font("sb", 40)
    w = d.textlength(text, font=f)
    x0 = x_right - w - 110
    d.rounded_rectangle((x0, y, x_right, y + 84), radius=42, fill=(245, 248, 246))
    d.ellipse((x0 + 34, y + 33, x0 + 52, y + 51), fill=accent)
    d.text((x0 + 70, y + 18), text, font=f, fill=(12, 26, 20))


def footer(d, idx, total=4):
    d.line((0, 1912, S, 1912), fill=(28, 52, 44), width=2)
    d.text((128, 1950), "Temply", font=font("b", 44), fill=TEXT)
    w = d.textlength("Temply", font=font("b", 44))
    d.text((128 + w, 1950), "works", font=font("b", 44), fill=BRAND)
    cx = S // 2 - (total * 34) // 2
    for i in range(total):
        d.ellipse((cx + i * 34, 1968, cx + i * 34 + 16, 1984), fill=BRAND if i == idx else (60, 84, 74))
    f = font("m", 34)
    for j, t in enumerate(["templyworks.com", "Notion template · instant access"]):
        w = d.textlength(t, font=f)
        d.text((S - 128 - w, 1934 + j * 46), t, font=f, fill=TEXT if j == 0 else MUTED)


def headline(d, x, y, lines, accent, size=132):
    f = font("xb", size)
    for i, (txt, acc) in enumerate(lines):
        cx = x
        for part, is_acc in acc_split(txt, acc):
            d.text((cx, y + i * int(size * 1.08)), part, font=f, fill=accent if is_acc else TEXT)
            cx += d.textlength(part, font=f)
    return y + len(lines) * int(size * 1.08)


def acc_split(txt, acc):
    if not acc or acc not in txt:
        return [(txt, False)]
    a, b = txt.split(acc, 1)
    return [(a, False), (acc, True), (b, False)]


def wrap(d, text, f, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) > width:
            lines.append(cur)
            cur = w
        else:
            cur = t
    lines.append(cur)
    return lines


def framed_shot(img, shot, box, title):
    """Paste a screenshot crop into a window frame at box=(x0,y0,x1,y1), cropping bottom."""
    x0, y0, x1, y1 = box
    W = x1 - x0
    bar = 64
    sh = shot.resize((W, int(shot.height * W / shot.width)), Image.LANCZOS)
    H = min(y1 - y0 - bar, sh.height)
    sh = sh.crop((0, 0, W, H))
    # shadow
    shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle((x0 + 10, y0 + 30, x1 + 10, y0 + bar + H + 40), 36, fill=(0, 0, 0, 170))
    img.paste(Image.alpha_composite(img.convert("RGBA"), shadow.filter(ImageFilter.GaussianBlur(40))).convert("RGB"))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((x0, y0, x1, y0 + bar + H), 30, fill=(32, 36, 35))
    for i, c in enumerate([(255, 95, 87), (254, 188, 46), (40, 200, 64)]):
        d.ellipse((x0 + 32 + i * 34, y0 + 24, x0 + 52 + i * 34, y0 + 44), fill=c)
    f = font("m", 28)
    w = d.textlength(title, font=f)
    d.text((x0 + (W - w) / 2, y0 + 17), title, font=f, fill=(170, 176, 174))
    mask = Image.new("L", sh.size, 255)
    img.paste(sh, (x0, y0 + bar), mask)
    d.line((x0, y0 + bar, x1, y0 + bar), fill=(50, 54, 53), width=2)


def load_crop(name, y0, y1, x0=0, x1=2880):
    return Image.open(os.path.join(SHOTS, name)).convert("RGB").crop((x0, y0, x1, y1))


def img_hero(p):
    a = p["accent"]
    img = bg(a)
    d = ImageDraw.Draw(img)
    logo(d, 128, 120)
    pill(d, S - 128, 108, p["name"], a)
    y = headline(d, 128, 300, p["hero"], a)
    f = font("r", 50)
    for i, ln in enumerate(wrap(d, p["sub"], f, 1700)):
        d.text((128, y + 40 + i * 68), ln, font=f, fill=(206, 222, 213))
    by = y + 40 + len(wrap(d, p["sub"], f, 1700)) * 68 + 40
    x = 128
    for b in ["Instant delivery", "Works on free Notion", "Lifetime access"]:
        fb = font("sb", 38)
        w = d.textlength(b, font=fb) + 104
        d.rounded_rectangle((x, by, x + w, by + 86), 43, fill=(18, 42, 34), outline=(44, 84, 68), width=2)
        d.ellipse((x + 34, by + 34, x + 52, by + 52), fill=a)
        d.text((x + 68, by + 20), b, font=fb, fill=TEXT)
        x += w + 24
    shot = load_crop(p["shot0"][0], *p["shot0"][1:])
    framed_shot(img, shot, (128, by + 150, S - 128, 1880), p["name"])
    footer(ImageDraw.Draw(img), 0)
    return img


def img_inside(p):
    a = p["accent"]
    img = bg(a)
    d = ImageDraw.Draw(img)
    logo(d, 128, 120)
    pill(d, S - 128, 108, p["name"], a)
    d.text((128, 290), "INSIDE THE TEMPLATE", font=font("sb", 40), fill=a)
    y = headline(d, 128, 350, p["inside"], a, size=118)
    f = font("r", 46)
    lines = wrap(d, p["inside_sub"], f, 1750)
    for i, ln in enumerate(lines):
        d.text((128, y + 30 + i * 62), ln, font=f, fill=(206, 222, 213))
    top = y + 30 + len(lines) * 62 + 60
    shot = load_crop(p["shot1"][0], *p["shot1"][1:])
    framed_shot(img, shot, (128, top, S - 128, 1860), p["name"])
    footer(ImageDraw.Draw(img), 1)
    return img


def img_features(p):
    a = p["accent"]
    img = bg(a)
    d = ImageDraw.Draw(img)
    logo(d, 128, 120)
    pill(d, S - 128, 108, p["name"], a)
    d.text((128, 290), "WHAT YOU GET", font=font("sb", 40), fill=a)
    headline(d, 128, 350, [("Everything you need.", None), ("Nothing you don't.", "Nothing you don't.")], a, size=118)
    cw, ch, gap = 880, 560, 32
    for i, (em, title, body) in enumerate(p["features"]):
        x = 128 + (i % 2) * (cw + gap)
        y = 700 + (i // 2) * (ch + gap)
        d.rounded_rectangle((x, y, x + cw, y + ch), 40, fill=CARD, outline=LINE, width=2)
        d.rounded_rectangle((x + 56, y + 56, x + 176, y + 176), 30, fill=tuple(int(c * .28) for c in a))
        e = emoji(em, 72)
        img.paste(e, (x + 116 - e.width // 2, y + 116 - e.height // 2), e)
        d.text((x + 56, y + 222), title, font=font("b", 56), fill=TEXT)
        fb = font("r", 40)
        for k, ln in enumerate(wrap(d, body, fb, cw - 112)):
            d.text((x + 56, y + 310 + k * 56), ln, font=fb, fill=MUTED)
    footer(d, 2)
    return img


def img_included(p):
    a = p["accent"]
    img = bg(a)
    d = ImageDraw.Draw(img)
    logo(d, 128, 120)
    pill(d, S - 128, 108, p["name"], a)
    d.text((128, 290), "WHAT'S INCLUDED", font=font("sb", 40), fill=a)
    headline(d, 128, 350, [("Ready in", None), ("5 minutes.", "5 minutes.")], a, size=118)
    # left: included list
    x0, y0 = 128, 700
    d.rounded_rectangle((x0, y0, x0 + 1040, 1840), 40, fill=CARD, outline=LINE, width=2)
    d.text((x0 + 56, y0 + 50), "Inside your copy", font=font("b", 52), fill=TEXT)
    fi = font("m", 40)
    for i, item in enumerate(p["included"]):
        yy = y0 + 150 + i * 92
        d.ellipse((x0 + 56, yy + 6, x0 + 100, yy + 50), fill=a)
        d.text((x0 + 66, yy + 3), "✓", font=font("b", 34), fill=BG)
        d.text((x0 + 128, yy), item, font=fi, fill=TEXT)
    # right: specs
    rx = x0 + 1040 + 32
    specs = [("Works on", "Notion Free, Plus & Business"), ("Devices", "Desktop, web & mobile app"),
             ("Delivery", p.get("delivery", "Instant — duplicate link + Quick-Start PDF")), ("Currency / region", p.get("region", "Any — fully editable")),
             ("Support", "info@templyworks.com")]
    d.rounded_rectangle((rx, y0, S - 128, 1840), 40, fill=CARD, outline=LINE, width=2)
    d.text((rx + 56, y0 + 50), "Details", font=font("b", 52), fill=TEXT)
    for i, (k, v) in enumerate(specs):
        yy = y0 + 160 + i * 205
        d.text((rx + 56, yy), k.upper(), font=font("sb", 30), fill=a)
        for j, ln in enumerate(wrap(d, v, font("m", 40), S - 128 - rx - 112)):
            d.text((rx + 56, yy + 46 + j * 52), ln, font=font("m", 40), fill=TEXT)
    footer(d, 3)
    return img


from products import PRODUCTS  # noqa: E402

if __name__ == "__main__":
    import sys
    only = sys.argv[1:]
    for p in PRODUCTS:
        if only and p["slug"] not in only:
            continue
        for k, fn in enumerate([img_hero, img_inside, img_features, img_included], 1):
            path = os.path.join(OUT, f"templyworks-{p['slug']}-0{k}-v2.png")
            fn(p).save(path, optimize=True)
            print(path)
