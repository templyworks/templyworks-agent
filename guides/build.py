import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import TEMPLATES, COMMON_START, COMMON_FAQ
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, PageBreak, KeepTogether, NextPageTemplate)

F = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", F + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", F + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVI", F + "DejaVuSans-Oblique.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("DV", normal="DV", bold="DVB", italic="DVI", boldItalic="DVB")

DARK = colors.HexColor("#0b1c15"); INK = colors.HexColor("#12211a")
PRIMARY = colors.HexColor("#1c5c3a"); ACCENT = colors.HexColor("#2f8f5b")
BRIGHT = colors.HexColor("#4fbe80"); PANEL = colors.HexColor("#e2f0e6")
MUTED = colors.HexColor("#5b6f66"); LINE = colors.HexColor("#d3e3d8")

EMO = {"🟢": '<font color="#2f8f5b">●</font>', "🟡": '<font color="#d9a400">●</font>',
       "🔴": '<font color="#d64545">●</font>', "✅": '<font color="#2f8f5b">✓</font>'}
def fx(s):
    for k, v in EMO.items(): s = s.replace(k, v)
    return s

st = {
 "h1": ParagraphStyle("h1", fontName="DVB", fontSize=17, leading=22, textColor=INK, spaceBefore=4, spaceAfter=10),
 "h2": ParagraphStyle("h2", fontName="DVB", fontSize=12, leading=16, textColor=PRIMARY, spaceBefore=12, spaceAfter=5),
 "body": ParagraphStyle("b", fontName="DV", fontSize=9.6, leading=14.5, textColor=INK),
 "muted": ParagraphStyle("m", fontName="DV", fontSize=9, leading=13.5, textColor=MUTED),
 "bullet": ParagraphStyle("bl", fontName="DV", fontSize=9.6, leading=14.5, textColor=INK, leftIndent=12, bulletIndent=0, spaceAfter=3),
 "cell": ParagraphStyle("c", fontName="DV", fontSize=9.2, leading=13.2, textColor=INK),
 "cellb": ParagraphStyle("cb", fontName="DVB", fontSize=9.2, leading=13.2, textColor=INK),
 "num": ParagraphStyle("n", fontName="DVB", fontSize=11, leading=14, textColor=colors.white, alignment=1),
}
W, H = A4; M = 18 * mm

def cover(c, doc):
    t = doc.tpl
    c.saveState()
    c.setFillColor(DARK); c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setFillColor(colors.HexColor("#123326")); c.circle(W * 0.85, H * 0.82, 140, stroke=0, fill=1)
    c.setFillColor(colors.HexColor("#0f2a1f")); c.circle(W * 0.1, H * 0.18, 110, stroke=0, fill=1)
    c.setFont("DVB", 15); c.setFillColor(colors.white); c.drawString(M, H - 30 * mm, "Temply")
    c.setFillColor(BRIGHT); c.drawString(M + c.stringWidth("Temply", "DVB", 15), H - 30 * mm, "works")
    c.setFillColor(BRIGHT); c.setFont("DVB", 9); c.drawString(M, H * 0.56, "SETUP & USER GUIDE")
    c.setFillColor(colors.white); c.setFont("DVB", 38); c.drawString(M, H * 0.56 - 48, t["name"])
    c.setFont("DV", 14); c.setFillColor(colors.HexColor("#b9d6c4")); c.drawString(M, H * 0.56 - 76, t["tagline"])
    c.setStrokeColor(ACCENT); c.setLineWidth(2); c.line(M, H * 0.56 - 96, M + 60, H * 0.56 - 96)
    c.setFont("DV", 9); c.setFillColor(colors.HexColor("#8fb39d"))
    c.drawString(M, 22 * mm, "templyworks.com  ·  info@templyworks.com")
    c.drawRightString(W - M, 22 * mm, "Notion template · Version Oct 2026")
    c.restoreState()

def page(c, doc):
    c.saveState()
    c.setFillColor(PRIMARY); c.rect(0, H - 6, W, 6, stroke=0, fill=1)
    c.setFont("DVB", 8.5); c.setFillColor(INK); c.drawString(M, H - 14 * mm, "Temply")
    c.setFillColor(ACCENT); c.drawString(M + c.stringWidth("Temply", "DVB", 8.5), H - 14 * mm, "works")
    c.setFont("DV", 8.5); c.setFillColor(MUTED); c.drawRightString(W - M, H - 14 * mm, doc.tpl["name"] + " — Guide")
    c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(M, 14 * mm, W - M, 14 * mm)
    c.drawString(M, 9 * mm, "Questions? info@templyworks.com")
    c.drawRightString(W - M, 9 * mm, str(doc.page))
    c.restoreState()

def steps(items):
    rows = []
    for i, (t, d) in enumerate(items, 1):
        rows.append([Paragraph(str(i), st["num"]), [Paragraph(t, st["cellb"]), Paragraph(fx(d), st["cell"])]])
    tb = Table(rows, colWidths=[9 * mm, W - 2 * M - 9 * mm])
    tb.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (0, -1), ACCENT), ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7), ("LEFTPADDING", (1, 0), (1, -1), 10),
        ("LINEBELOW", (0, 0), (-1, -2), 4, colors.white),
        ("BACKGROUND", (1, 0), (1, -1), colors.HexColor("#f4f8f5"))]))
    return tb

def kv(items, head=None):
    rows = [[Paragraph(k, st["cellb"]), Paragraph(fx(v), st["cell"])] for k, v in items]
    tb = Table(rows, colWidths=[42 * mm, W - 2 * M - 42 * mm])
    tb.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), 0.5, LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6), ("LEFTPADDING", (0, 0), (-1, -1), 2)]))
    return tb

def callout(text):
    tb = Table([[Paragraph(fx(text), st["body"])]], colWidths=[W - 2 * M])
    tb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), PANEL), ("LINEBEFORE", (0, 0), (0, -1), 3, ACCENT),
        ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 9), ("LEFTPADDING", (0, 0), (-1, -1), 12)]))
    return tb

def bullets(lst):
    return [Paragraph(fx(b), st["bullet"], bulletText="•") for b in lst]

def build(t, out):
    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=22 * mm, bottomMargin=20 * mm,
                          title=f"{t['name']} — Guide", author="Templyworks", subject="Notion template guide")
    doc.tpl = t
    fr = Frame(M, 20 * mm, W - 2 * M, H - 42 * mm, id="f")
    doc.addPageTemplates([PageTemplate("cover", frames=[Frame(0, 0, W, H)], onPage=cover),
                          PageTemplate("page", frames=[fr], onPage=page)])
    s = [NextPageTemplate("page"), PageBreak()]
    s += [Paragraph("Welcome", st["h1"]), Paragraph(t["intro"], st["body"]), Spacer(1, 8),
          Paragraph("What's inside", st["h2"]), kv(t["inside"]), Spacer(1, 6),
          Paragraph("Get started in 5 minutes", st["h2"]), steps(COMMON_START + t["setup"]), Spacer(1, 10),
          callout("<b>Good to know:</b> fields with a formula or rollup fill in by themselves — you never type into them. "
                  "If one shows empty, the linked data (relation, date or amount) it needs is missing.")]
    s.append(PageBreak())
    s.append(Paragraph("How it works", st["h1"]))
    for title, lst in t["sections"]:
        s.append(KeepTogether([Paragraph(title, st["h2"])] + bullets(lst)))
    s.append(Spacer(1, 6))
    s.append(KeepTogether([Paragraph("Your routine", st["h2"]), kv(t["routine"])]))
    s.append(KeepTogether([Paragraph("Pro tips", st["h2"])] + bullets(t["tips"])))
    s.append(KeepTogether([Paragraph("FAQ", st["h2"]), kv(COMMON_FAQ)]))
    s += [Spacer(1, 12), Paragraph("Licence: personal and business use, including work for your own clients. "
          "Reselling or redistributing the template is not allowed. Digital product — all sales are final once delivered "
          "(you agreed to immediate delivery at checkout). Statutory rights for defective content remain unaffected.", st["muted"])]
    doc.build(s)

if __name__ == "__main__":
    outdir = sys.argv[1]; os.makedirs(outdir, exist_ok=True)
    for t in TEMPLATES:
        p = os.path.join(outdir, f"Templyworks-{t['name'].replace(' ', '-')}-Guide.pdf"); build(t, p); print(p)
