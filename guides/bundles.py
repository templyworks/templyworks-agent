"""Bundle guides = bundle intro (cover + overview page) + the full guides of the included templates."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import build as B
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, NextPageTemplate
from reportlab.lib.units import mm
from pypdf import PdfReader, PdfWriter

BUNDLES = [
    {"name": "Client Machine", "file": "Client-Machine", "tagline": "Win clients. Run clients. Look professional doing it.",
     "intro": "Three Notion templates that cover the whole client lifecycle — from first pitch to final invoice. This guide starts with how the three work together, followed by the full guide for each template.",
     "parts": [("Client Pipeline", "Client-Pipeline", "Find and follow up with leads — contacts, deals, every call and email."),
               ("Pitch Kit", "Pitch-Kit", "Turn interest into a signed proposal — services library, example proposal, proof bank, follow-up scripts."),
               ("Client Portal", "Client-Portal", "Deliver the work — milestones, files, feedback and invoices on one shared page.")],
     "flow": [("Lead comes in", "Add the person in <b>Client Pipeline → Contacts</b> and log the first call or email in the Interaction Log with a follow-up date."),
              ("Send a proposal", "Create the proposal in <b>Pitch Kit</b>, link services from your library, send it and set a follow-up date. Move the deal to <b>Proposal Sent</b> in Client Pipeline."),
              ("Deal won", "Mark the proposal <b>Accepted</b> and the deal <b>Closed Won</b>. Add a project in Client Pipeline → Projects."),
              ("Deliver", "Duplicate a <b>Client Portal</b> for the client, fill in Project at a glance, add milestones and the first invoice, and share it with <b>Can comment</b>.")],
     "order": "Set up in this order: Pitch Kit services library first (10 min), then Client Pipeline, then one Client Portal per client when you win work."},
    {"name": "Solo Ops", "file": "Solo-Ops", "tagline": "Your money, your work, your brain — all in order.",
     "intro": "Three Notion templates that run the parts of your business nobody else sees. This guide starts with how the three work together, followed by the full guide for each template.",
     "parts": [("Finance HQ", "Finance-HQ", "Money in and out, automatic budgets, bills, goals and net worth."),
               ("Project Tracker", "Project-Tracker", "Projects, tasks, scope changes and time with automatic progress and health."),
               ("Second Brain", "Second-Brain", "Capture everything, sort it with PARA, keep ideas and processes in one place.")],
     "flow": [("Daily", "Capture ideas and notes into <b>Second Brain → Inbox</b>. Work from <b>Project Tracker → This week</b> and log your hours. Log spending in <b>Finance HQ</b>."),
              ("Weekly", "Sunday Weekly Review in Second Brain, check project <b>Health</b>, check budget <b>Status</b> and bills coming up."),
              ("Monthly", "Update account balances in Finance HQ, compare logged vs quoted hours, archive finished projects, turn repeated work into SOPs.")],
     "order": "Set up in this order: Finance HQ budgets (5 min), Project Tracker with your current projects, then start capturing into Second Brain."},
]

def intro_pdf(b, out):
    doc = BaseDocTemplate(out, pagesize=B.A4, leftMargin=B.M, rightMargin=B.M, topMargin=22 * mm, bottomMargin=20 * mm,
                          title=f"{b['name']} — Bundle Guide", author="Templyworks")
    doc.tpl = {"name": b["name"], "tagline": b["tagline"], "cover_label": "BUNDLE GUIDE · 3 TEMPLATES"}
    fr = Frame(B.M, 20 * mm, B.W - 2 * B.M, B.H - 42 * mm)
    doc.addPageTemplates([PageTemplate("cover", frames=[Frame(0, 0, B.W, B.H)], onPage=B.cover),
                          PageTemplate("page", frames=[fr], onPage=B.page)])
    st = B.st
    s = [NextPageTemplate("page"), PageBreak(),
         Paragraph("Welcome", st["h1"]), Paragraph(b["intro"], st["body"]), Spacer(1, 8),
         Paragraph("What's in your bundle", st["h2"]), B.kv([(n, d) for n, _, d in b["parts"]]), Spacer(1, 6),
         Paragraph("How they work together", st["h2"]), B.steps(b["flow"]), Spacer(1, 10),
         B.callout("<b>Where to start:</b> " + b["order"]), Spacer(1, 10),
         Paragraph("Each template has its own link in your delivery email — duplicate all three into your workspace. "
                   "The full guide for each template follows on the next pages.", st["muted"])]
    doc.build(s)

if __name__ == "__main__":
    outdir = sys.argv[1]; tmp = os.path.join(outdir, "_tmp_intro.pdf")
    for b in BUNDLES:
        intro_pdf(b, tmp)
        w = PdfWriter()
        for p in [tmp] + [os.path.join(outdir, f"Templyworks-{f}-Guide.pdf") for _, f, _ in b["parts"]]:
            for pg in PdfReader(p).pages: w.add_page(pg)
        w.add_metadata({"/Title": f"{b['name']} — Bundle Guide", "/Author": "Templyworks"})
        out = os.path.join(outdir, f"Templyworks-{b['file']}-Bundle-Guide.pdf")
        with open(out, "wb") as f: w.write(f)
        print(out)
    os.remove(tmp)
