"""Generate Templyworks Notion cover images (1500x600) — v4 with real sample data.

No title/tagline on the cover: the Notion page shows them right below.
Content stays in the visible band (y ~185-390); bottom-left stays free for the page icon.
"""
import glob, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1500, 600
BG = (6, 18, 16)
CARD = (13, 31, 27)
CARD_LINE = (36, 74, 62)
TEXT = (236, 244, 239)
MUTED = (140, 168, 154)


def font(size, bold=False):
    names = (["Inter-Bold", "DejaVuSans-Bold", "LiberationSans-Bold"] if bold
             else ["Inter-Regular", "DejaVuSans", "LiberationSans-Regular"])
    for n in names:
        hits = glob.glob(f"/usr/share/fonts/**/{n}.ttf", recursive=True)
        if hits:
            return ImageFont.truetype(hits[0], size)
    return ImageFont.load_default()


# slug, accent colour, cards: (title, [(label, value, highlight?)...])
TEMPLATES = [
    ("finance-hq", (72, 196, 128), [
        ("Net worth", [("Total", "13,600", True), ("Debt", "−7,840", False)]),
        ("Budgets", [("Groceries", "248 left", True), ("Dining", "89 left", False)]),
        ("Bills due", [("Cloud 2TB", "Oct 22", False), ("Gym", "Oct 28", False)]),
        ("This month", [("In", "5,050", True), ("Out", "1,830", False)]),
    ]),
    ("client-pipeline", (88, 170, 230), [
        ("Follow up", [("Bloom Yoga", "today", True), ("Aurora", "Oct 19", False)]),
        ("Pipeline", [("Open deals", "4", False), ("Value", "$15,900", True)]),
        ("Won", [("Nordic Health", "$14,000", True), ("This year", "1", False)]),
        ("Next step", [("Aurora", "15-min call", False), ("Lumen", "new quote", False)]),
    ]),
    ("project-tracker", (236, 196, 72), [
        ("Due this week", [("Logo files", "Oct 17", True), ("Review call", "Oct 22", False)]),
        ("Health", [("Aurora", "On track", True), ("Saffron", "At risk", False)]),
        ("Scope changes", [("Approved", "+$475", True), ("Waiting", "$380", False)]),
        ("Time", [("Logged", "64 h", False), ("Billable", "93%", True)]),
    ]),
    ("pitch-kit", (190, 140, 245), [
        ("Packages", [("Good", "$2,500", False), ("Better ★", "$6,500", True)]),
        ("Follow up", [("Aurora", "Oct 17", True), ("Lumen Café", "Oct 19", False)]),
        ("Proposals", [("Accepted", "2", True), ("Open", "2", False)]),
        ("Proof", [("Clinic", "3× bookings", True), ("Bistro", "+18% AOV", False)]),
    ]),
    ("second-brain", (240, 140, 185), [
        ("Inbox", [("To process", "3", True), ("Filed", "4", False)]),
        ("Projects", [("Portfolio site", "Nov 15", True), ("Run a 10k", "Mar 1", False)]),
        ("Areas", [("Clients & Work", "Weekly", False), ("Money", "Monthly", False)]),
        ("Weekly review", [("Inbox cleared", "✓", True), ("Top 3 set", "✓", True)]),
    ]),
    ("client-portal", (214, 160, 112), [
        ("Coming up", [("Logo v2 review", "Oct 20", True), ("Finals", "Oct 30", False)]),
        ("For review", [("Logo refinement", "v2", True), ("Brand guide", "draft", False)]),
        ("Feedback", [("Warmer palette?", "open", True), ("Typography", "done", False)]),
        ("Invoices", [("Paid", "$5,000", True), ("Next due", "Nov 5", False)]),
    ]),
    ("student-os", (246, 160, 100), [
        ("Due this week", [("Read ch. 4–6", "3 days", True), ("Problem set 5", "4 days", False)]),
        ("Next exams", [("Calculus quiz", "8 days", True), ("Bio midterm", "19 days", False)]),
        ("Grades", [("GPA", "3.3", True), ("English Lit", "A−", False)]),
        ("Study time", [("This week", "2h 20m", True), ("Calculus", "75 min", False)]),
    ]),
]


def rounded(d, box, r, fill, outline=None, width=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def text_right(d, x_right, y, txt, f, fill):
    w = d.textlength(txt, font=f)
    d.text((x_right - w, y), txt, font=f, fill=fill)


def make(slug, accent, cards, out_dir):
    img = Image.new("RGB", (W, H), BG)
    glow = Image.new("RGB", (W, H), BG)
    gd = ImageDraw.Draw(glow)
    ar, ag, ab = accent
    gd.ellipse((950, -350, 1800, 450), fill=(18, 70, 48))
    gd.ellipse((150, 60, 1000, 560), fill=(int(ar * .26), int(ag * .26), int(ab * .26)))
    img = Image.blend(img, glow.filter(ImageFilter.GaussianBlur(140)), 1.0)
    d = ImageDraw.Draw(img)
    for x in range(0, W, 30):
        for y in range(0, H, 30):
            d.point((x, y), fill=(22, 44, 37))

    cw, ch, gap = 262, 158, 20
    total = 4 * cw + 3 * gap
    cx = (W - total) // 2 + 60
    cy = 214
    d.text((cx, 178), "TEMPLYWORKS", font=font(18, True), fill=(120, 201, 150))

    f_title = font(20, True)
    f_label = font(17)
    f_value = font(19, True)
    for i, (title, rows) in enumerate(cards):
        bx = cx + i * (cw + gap)
        by = cy
        rounded(d, (bx, by, bx + cw, by + ch), 18, CARD, outline=CARD_LINE, width=2)
        rounded(d, (bx + 20, by + 22, bx + 25, by + 42), 2, accent)
        d.text((bx + 34, by + 19), title, font=f_title, fill=TEXT)
        for k in range(3):
            yy = by + 70 + k * 26
            rounded(d, (bx + 20, yy, bx + 20 + (170 - k * 45), yy + 10), 5, (24, 52, 44))
            a = accent if (i + k) % 3 else tuple(min(255, int(c * 1.25)) for c in accent)
            d.ellipse((bx + cw - 36, yy - 2, bx + cw - 22, yy + 12), fill=a)
    path = os.path.join(out_dir, f"cover-{slug}-v6.png")
    img.save(path, optimize=True)
    return path


if __name__ == "__main__":
    out = os.path.dirname(os.path.abspath(__file__))
    for t in TEMPLATES:
        print(make(*t, out))
