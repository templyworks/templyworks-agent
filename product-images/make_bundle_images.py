"""Bundle images (2048x2048) in the v2 style: hero + inside."""
import os
from PIL import Image, ImageDraw
import make_product_images as m
from products import PRODUCTS

P = {p["slug"]: p for p in PRODUCTS}
BUNDLES = [
    dict(slug="client-machine", name="Client Machine", accent=m.BRAND,
         hero=[("Win clients.", None), ("Run clients.", "Run clients.")],
         sub="Three Notion templates for the whole client lifecycle — from first pitch to final invoice.",
         items=["client-pipeline", "pitch-kit", "client-portal"],
         roles=["Find & follow up", "Pitch & close", "Deliver & get paid"]),
    dict(slug="solo-ops", name="Solo Ops", accent=m.BRAND,
         hero=[("Your money, work", None), ("and brain in order.", "in order")],
         sub="Three Notion templates that run the parts of your business nobody else sees.",
         items=["finance-hq", "project-tracker", "second-brain"],
         roles=["Money", "Work", "Notes & ideas"]),
]


def badges(d, y, labels, a):
    x = 128
    for b in labels:
        fb = m.font("sb", 38)
        w = d.textlength(b, font=fb) + 104
        d.rounded_rectangle((x, y, x + w, y + 86), 43, fill=(18, 42, 34), outline=(44, 84, 68), width=2)
        d.ellipse((x + 34, y + 34, x + 52, y + 52), fill=a)
        d.text((x + 68, y + 20), b, font=fb, fill=m.TEXT)
        x += w + 24


def hero(b):
    img = m.bg(b["accent"])
    d = ImageDraw.Draw(img)
    m.logo(d, 128, 120)
    m.pill(d, S - 128, 108, b["name"] + " bundle", b["accent"])
    y = m.headline(d, 128, 300, b["hero"], b["accent"])
    f = m.font("r", 50)
    lines = m.wrap(d, b["sub"], f, 1700)
    for i, ln in enumerate(lines):
        d.text((128, y + 40 + i * 68), ln, font=f, fill=(206, 222, 213))
    by = y + 40 + len(lines) * 68 + 40
    badges(d, by, ["3 templates", "Save over 20%", "Works on free Notion"], b["accent"])
    # three framed shots side by side
    top = by + 160
    w, gap = 576, 32
    for i, slug in enumerate(b["items"]):
        p = P[slug]
        x0 = 128 + i * (w + gap)
        d.text((x0 + 4, top), p["name"], font=m.font("b", 46), fill=p["accent"])
        d.text((x0 + 4, top + 60), b["roles"][i], font=m.font("m", 34), fill=m.MUTED)
        shot = m.load_crop(p["shot0"][0], 700, 2200, 0, 1900)
        m.framed_shot(img, shot, (x0, top + 130, x0 + w, 1860), p["name"])
        d = ImageDraw.Draw(img)
    m.footer(d, 0, 2)
    return img


def inside(b):
    img = m.bg(b["accent"])
    d = ImageDraw.Draw(img)
    m.logo(d, 128, 120)
    m.pill(d, S - 128, 108, b["name"] + " bundle", b["accent"])
    d.text((128, 290), "WHAT'S INSIDE", font=m.font("sb", 40), fill=b["accent"])
    m.headline(d, 128, 350, [("Three templates.", None), ("One system.", "One system.")], b["accent"], size=118)
    y0, ch, gap = 700, 360, 30
    for i, slug in enumerate(b["items"]):
        p = P[slug]
        a = p["accent"]
        y = y0 + i * (ch + gap)
        d.rounded_rectangle((128, y, S - 128, y + ch), 40, fill=m.CARD, outline=m.LINE, width=2)
        d.rounded_rectangle((128, y, 148, y + ch), 10, fill=a)
        d.text((200, y + 46), p["name"], font=m.font("b", 60), fill=m.TEXT)
        d.text((200, y + 124), b["roles"][i], font=m.font("sb", 36), fill=a)
        fb = m.font("r", 36)
        for k, (em, title, body) in enumerate(p["features"][:3]):
            yy = y + 190 + k * 52
            d.ellipse((200, yy + 12, 216, yy + 28), fill=a)
            d.text((236, yy), title + " — " + body, font=fb, fill=(206, 222, 213))
    m.footer(d, 1, 2)
    return img


S = m.S
if __name__ == "__main__":
    for b in BUNDLES:
        for k, fn in enumerate([hero, inside], 1):
            path = os.path.join(m.OUT, f"templyworks-{b['slug']}-0{k}-v2.png")
            fn(b).save(path, optimize=True)
            print(path)
