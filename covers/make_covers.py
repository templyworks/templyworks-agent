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

    # No title/tagline: the Notion page already shows them right below the cover.
    # Keep content in the visible band (y ~185-390); leave bottom-left free for the icon.
    cw, ch, gap = 250, 150, 22
    total = 4 * cw + 3 * gap
    cx = (W - total) // 2 + 60
    cy = 215
    d.text((cx, 178), "TEMPLYWORKS", font=font(18, True), fill=GREEN_LT)
    for i, label in enumerate(cards):
        bx = cx + i * (cw + gap)
        by = cy
        rounded(d, (bx, by, bx + cw, by + ch), 18, CARD, outline=(34, 72, 60), width=2)
        d.text((bx + 20, by + 18), label, font=font(21, True), fill=TEXT)
        for k in range(3):
            yy = by + 62 + k * 26
            rounded(d, (bx + 20, yy, bx + 20 + (160 - k * 40), yy + 10), 5, CARD2)
            d.ellipse((bx + cw - 36, yy - 2, bx + cw - 22, yy + 12),
                      fill=GREEN if (i + k) % 3 else GREEN_LT)
    path = os.path.join(out_dir, f"cover-{slug}-v3.png")
    img.save(path, optimize=True)
    return path

if __name__ == "__main__":
    out = os.path.dirname(os.path.abspath(__file__))
    for t in TEMPLATES:
        print(make(*t, out))
