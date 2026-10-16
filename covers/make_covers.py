"""Generate Templyworks Notion cover images (1500x600) for each template."""
import glob, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1500, 600
BG = (6, 18, 16)
GREEN = (47, 143, 91)
GREEN_LT = (120, 201, 150)
CARD = (14, 34, 29)
CARD2 = (20, 48, 40)
TEXT = (236, 244, 239)
MUTED = (150, 178, 164)

def font(size, bold=False):
    names = (["Inter-Bold", "DejaVuSans-Bold", "LiberationSans-Bold"] if bold
             else ["Inter-Regular", "DejaVuSans", "LiberationSans-Regular"])
    for n in names:
        hits = glob.glob(f"/usr/share/fonts/**/{n}.ttf", recursive=True)
        if hits:
            return ImageFont.truetype(hits[0], size)
    return ImageFont.load_default()

TEMPLATES = [
    ("finance-hq", "Finance HQ", "Budgets, bills, goals & net worth — calmly.",
     ["Net worth", "Budgets", "Bills due", "This month"]),
    ("client-pipeline", "Client Pipeline", "Leads, deals & follow-ups — nothing goes cold.",
     ["Prospect", "Contacted", "Proposal", "Won"]),
    ("project-tracker", "Project Tracker", "Every deadline, every client, one calm view.",
     ["Due this week", "Project health", "Scope changes", "Time log"]),
    ("pitch-kit", "Pitch Kit", "Proposals, proof & follow-ups that close.",
     ["Good", "Better", "Best", "Follow up"]),
    ("second-brain", "Second Brain", "Capture fast. File later. Find anything.",
     ["Inbox", "Projects", "Areas", "Weekly review"]),
    ("client-portal", "Client Portal", "One home for your client: status, files, invoices.",
     ["Coming up", "For review", "Feedback", "Invoices"]),
    ("student-os", "Student OS", "Classes, assignments, exams & GPA in one place.",
     ["Due this week", "Next exams", "GPA", "Study time"]),
]

def rounded(d, box, r, fill, outline=None, width=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)

def make(slug, name, tagline, cards, out_dir):
    img = Image.new("RGB", (W, H), BG)
    # soft green glow top-right
    glow = Image.new("RGB", (W, H), BG)
    gd = ImageDraw.Draw(glow)
    gd.ellipse((900, -350, 1750, 450), fill=(18, 70, 48))
    gd.ellipse((-300, 380, 500, 1000), fill=(12, 40, 30))
    img = Image.blend(img, glow.filter(ImageFilter.GaussianBlur(140)), 1.0)
    d = ImageDraw.Draw(img)
    # dotted grid
    for x in range(0, W, 30):
        for y in range(0, H, 30):
            d.point((x, y), fill=(22, 44, 37))

    # left text block (kept inside the centre band Notion shows on narrow screens)
    x0 = 140
    d.text((x0, 150), "TEMPLYWORKS", font=font(22, True), fill=GREEN_LT)
    d.rectangle((x0, 186, x0 + 56, 190), fill=GREEN)
    d.text((x0 - 4, 215), name, font=font(84, True), fill=TEXT)
    d.text((x0, 330), tagline, font=font(28), fill=MUTED)
    rounded(d, (x0, 395, x0 + 262, 445), 25, GREEN)
    d.text((x0 + 24, 404), "Notion template", font=font(24, True), fill=(255, 255, 255))

    # right: mock UI cards
    cx, cy = 900, 120
    cw, ch, gap = 230, 160, 24
    for i, label in enumerate(cards):
        col, row = i % 2, i // 2
        bx = cx + col * (cw + gap)
        by = cy + row * (ch + gap)
        rounded(d, (bx, by, bx + cw, by + ch), 18, CARD, outline=(34, 72, 60), width=2)
        d.text((bx + 20, by + 18), label, font=font(22, True), fill=TEXT)
        # fake rows
        for k in range(3):
            yy = by + 62 + k * 28
            rounded(d, (bx + 20, yy, bx + 20 + (150 - k * 30), yy + 12), 6, CARD2)
            d.ellipse((bx + cw - 38, yy - 2, bx + cw - 22, yy + 14),
                      fill=GREEN if (i + k) % 3 else GREEN_LT)
    path = os.path.join(out_dir, f"cover-{slug}.png")
    img.save(path, optimize=True)
    return path

if __name__ == "__main__":
    out = os.path.dirname(os.path.abspath(__file__))
    for t in TEMPLATES:
        print(make(*t, out))
