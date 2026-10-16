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

    # Notion crops covers to a centre band (~y 170-430) and puts the page icon
    # bottom-left, so keep everything in y 185-375 and nothing low on the left.
    x0 = 150
    d.text((x0, 188), "TEMPLYWORKS", font=font(20, True), fill=GREEN_LT)
    d.rectangle((x0, 218, x0 + 48, 221), fill=GREEN)
    d.text((x0 - 3, 232), name, font=font(72, True), fill=TEXT)
    d.text((x0, 322), tagline, font=font(26), fill=MUTED)

    # right: 2x2 mock cards, vertically centred
    cw, ch, gap = 176, 84, 14
    cx = W - 120 - 2 * cw - gap
    cy = 205
    for i, label in enumerate(cards):
        bx = cx + (i % 2) * (cw + gap)
        by = cy + (i // 2) * (ch + gap)
        rounded(d, (bx, by, bx + cw, by + ch), 14, CARD, outline=(34, 72, 60), width=2)
        d.text((bx + 14, by + 12), label, font=font(17, True), fill=TEXT)
        for k in range(2):
            yy = by + 44 + k * 20
            rounded(d, (bx + 14, yy, bx + 14 + (110 - k * 30), yy + 9), 4, CARD2)
            d.ellipse((bx + cw - 28, yy - 2, bx + cw - 16, yy + 10),
                      fill=GREEN if (i + k) % 3 else GREEN_LT)
    path = os.path.join(out_dir, f"cover-{slug}-v2.png")
    img.save(path, optimize=True)
    return path

if __name__ == "__main__":
    out = os.path.dirname(os.path.abspath(__file__))
    for t in TEMPLATES:
        print(make(*t, out))
