"""Amazon-style Shopify descriptions for the 7 Templyworks products. Run → descriptions.json"""
import json, html

COMMON_SPECS = [
    ("Format", "Notion template (duplicate link)"),
    ("Notion plan", "Works on Notion Free, Plus and Business"),
    ("Devices", "Desktop, web, iPhone, iPad and Android (Notion app)"),
    ("Delivery", "Instant — link on the order page and by email"),
    ("Setup time", "About 5 minutes"),
    ("Support", "info@templyworks.com"),
]

COMMON_FAQ = [
    ("Do I need a paid Notion plan?", "No. Everything works on Notion's free plan."),
    ("How do I get it?", "Right after checkout you get a link. Open it, click Duplicate, and the template is in your own Notion workspace."),
    ("Can I change it?", "Yes. Every page, database and property is fully editable."),
    ("Can I get a refund?", "You agree to instant delivery at checkout, so all sales are final once your link is delivered. Your statutory rights for faulty or not-as-described content are unaffected. If something doesn't work, email us — we'll fix it."),
]

P = {
"finance-hq": dict(
  gid="gid://shopify/Product/16245061583197",
  title="Finance HQ — Notion Budget Planner & Personal Finance Tracker (Budgets, Bills, Net Worth)",
  seo_title="Finance HQ — Notion Budget & Finance Tracker | Templyworks",
  seo_desc="Notion budget planner: track transactions, monthly budgets, bills, savings goals and net worth in one calm page. Any currency. Works on free Notion.",
  intro="See where every dollar goes — without a spreadsheet. Finance HQ puts your spending, budgets, bills, savings goals and net worth on one calm Notion page, and does the maths for you.",
  bullets=[
    ("LOG IN 10 SECONDS", "Add income or an expense with a date, category and amount. This month's totals for money in and money out update by themselves."),
    ("BUDGETS THAT TRACK THEMSELVES", "Set a monthly limit per category once. Spent, remaining, used % and status (Healthy / Watch / Over) update live and reset every month."),
    ("NET WORTH IN ONE NUMBER", "List your accounts, savings and debts. Credit cards and loans count as debt automatically, and your net worth adds itself up."),
    ("NO SURPRISE BILLS", "Every subscription and bill in one list. Yearly plans are shown as a monthly cost, and you see what renews in the next 30 days."),
    ("SAVINGS GOALS", "Emergency fund, tax reserve, that trip — set a target and watch the progress %."),
    ("ANY CURRENCY, FREE NOTION", "Amounts are plain numbers, so it works with dollars, euros, pounds or anything else. Runs fully on Notion's free plan; optional bonus charts for paid plans."),
  ],
  desc=[
    "Most budget apps want your bank login. Most spreadsheets break the first time you add a row. Finance HQ is the calm middle: a private Notion page you fill in yourself, with the formulas already done.",
    "The page opens with an <strong>At a glance</strong> row — net worth, bills coming up and a budget check — so one look tells you how you're doing. Below sit your Transactions, Budgets, Goals, Accounts and Subscriptions, all linked together.",
    "Built for freelancers, young professionals and anyone who wants to understand their money in 2 minutes a week.",
  ],
  included=["Transactions tracker (this month, all, income, expenses views)", "Monthly budgets with live status", "Goals & savings pots", "Accounts & net worth", "Subscriptions & bills with next payment dates", "This-month totals (money in / money out)", "Bonus charts & visual dashboard (paid Notion plans)", "Example data so you see how it works", "Quick-Start PDF guide"],
  specs=[("Currency", "Any — amounts are plain numbers")],
  faq=[("Do I need a paid Notion plan?", "No. Everything works on the free plan; only the optional bonus charts need a paid Notion plan."), ("Does it connect to my bank?", "No. You stay in control and add transactions yourself — it takes about 10 seconds each. Nothing is shared with anyone.")],
),
"client-pipeline": dict(
  gid="gid://shopify/Product/16246055371101",
  title="Client Pipeline — Notion CRM for Freelancers (Leads, Deals, Follow-ups & Contacts)",
  seo_title="Client Pipeline — Notion CRM for Freelancers | Templyworks",
  seo_desc="Simple Notion CRM for freelancers: contacts, deal pipeline, interaction log and follow-up dates so no lead goes cold. Works on free Notion. Instant delivery.",
  intro="Never let a lead go cold again. Client Pipeline is a simple Notion CRM that shows who to follow up with today, where every deal stands and what the next step is.",
  bullets=[
    ("KNOW WHO TO REPLY TO TODAY", "The Today's focus section lists every follow-up that is due, so warm leads never go quiet."),
    ("DEAL PIPELINE BOARD", "Drag deals from Prospect to Closed Won. Every card shows its value and next step, so nothing stalls."),
    ("CONTACTS THAT UPDATE THEMSELVES", "Last contacted date and total pipeline value fill in automatically from your deals and interactions."),
    ("LOG EVERY CALL AND EMAIL", "One row per interaction, with notes and a follow-up date. Your whole client history in one place."),
    ("FROM WON DEAL TO PROJECT", "Turn a won deal into a project with due date and budget, linked to the right client."),
    ("NO CRM BLOAT", "No seats, no monthly fee, no setup consultant. It runs on Notion's free plan."),
  ],
  desc=[
    "If your leads live in your inbox, some of them are slipping. Client Pipeline gives every lead a home, every deal a next step and every follow-up a date.",
    "Open the page in the morning, check <strong>Today's focus</strong>, send your messages and move on. That's the whole routine — about 5 minutes a day.",
    "Built for freelancers, consultants and small studios who want a CRM they will actually use.",
  ],
  included=["Contacts database", "Deals pipeline board (Prospect → Closed Won)", "Interaction log with follow-up dates", "Follow-up calendar", "Projects for won deals", "Today's focus section", "Example data so you see how it works", "Quick-Start PDF guide"],
  specs=[("Currency", "Any — values are plain numbers")],
  faq=[("Can I import my existing contacts?", "Yes. Notion can import a CSV straight into the Contacts database.")],
),
"project-tracker": dict(
  gid="gid://shopify/Product/16246056354141",
  title="Project Tracker — Notion Project Management Template (Tasks, Deadlines, Time & Scope)",
  seo_title="Project Tracker — Notion Project Template | Templyworks",
  seo_desc="Notion project tracker for freelancers: projects, tasks by phase, deadlines, scope changes and time log with automatic project health. Works on free Notion.",
  intro="Every deadline. Every client. One page. Project Tracker shows what's due this week, which projects are at risk and whether your hours match the quote — automatically.",
  bullets=[
    ("SEE THIS WEEK IN ONE GLANCE", "Every task due in the next 7 days, across every client, sorted by deadline."),
    ("PROJECT HEALTH ON AUTOPILOT", "On Track, At Risk or Overdue — calculated from deadline, progress and hours. No status meetings with yourself."),
    ("TASKS BY PHASE", "Discovery → Design → Review → Delivery. Tick a task off and the project progress updates. Late tasks turn red on their own."),
    ("STOP SCOPE CREEP", "Log every extra request, price it, and start only when the client says yes."),
    ("QUOTED VS LOGGED HOURS", "Log time with rates and see if a project is still profitable — then price the next one better."),
    ("BOARD, TIMELINE OR BY CLIENT", "Switch views in one click. Runs on Notion's free plan."),
  ],
  desc=[
    "Juggling three or more client projects in your head doesn't scale. Project Tracker gives you one place for projects, tasks, scope changes and hours — and tells you which project needs attention.",
    "Start your day with <strong>This week</strong>, work through your tasks and log your hours as you go. Health and progress take care of themselves.",
    "Built for freelancers, solo studios and small teams running several projects at once.",
  ],
  included=["Projects (board, timeline and by-client views)", "Tasks by phase with automatic overdue flags", "Scope change log", "Time log with hourly rates", "This-week section", "Example data so you see how it works", "Quick-Start PDF guide"],
  specs=[],
  faq=[("Does it work for a team?", "Yes. Share the page with your team in Notion and assign tasks to each other. Teams of 2+ may need Notion Plus for unlimited content.")],
),
"pitch-kit": dict(
  gid="gid://shopify/Product/16246061105501",
  title="Pitch Kit — Notion Proposal Template for Freelancers (Services, Pricing, Follow-ups)",
  seo_title="Pitch Kit — Notion Proposal & Pricing Template | Templyworks",
  seo_desc="Notion proposal system: Good/Better/Best services library, written example proposal, proof bank, follow-up scripts and pipeline. Works on free Notion.",
  intro="Send proposals that close. Pitch Kit gives you a Good/Better/Best services library, a fully written example proposal, a proof bank and copy-and-send follow-up scripts — plus a pipeline to track every proposal.",
  bullets=[
    ("A PROPOSAL YOU CAN COPY", "A complete example proposal built on 7 steps: Problem, Solution, Why me, Deliverables, Timeline, Pricing, Next step. Duplicate it for each new client."),
    ("GOOD / BETTER / BEST PACKAGES", "Build your service packages once. Link them to a proposal and the price adds up by itself."),
    ("TRACK EVERY PROPOSAL", "Draft → Sent → Viewed → Accepted or Rejected on one board, with your win rate calculated for you."),
    ("NEVER FORGET TO FOLLOW UP", "Every proposal has a follow-up date. The Follow up now list shows who to nudge today."),
    ("FOLLOW-UP SCRIPTS", "Ready-to-send messages for every stage — from \"thanks for the call\" to \"welcome aboard\" and the polite \"it's too expensive\" reply."),
    ("PROOF BANK", "Case studies with problem, result and quote, ready to link into any proposal."),
  ],
  desc=[
    "Most deals aren't lost on the call — they're lost after the proposal, in the silence. Pitch Kit fixes both sides: a proposal that's easy to say yes to, and a follow-up system so you never just wait.",
    "Your routine: send the proposal within 24 hours of the call, then check <strong>Follow up now</strong> each morning and nudge with a script.",
    "Built for freelancers, consultants and agencies who are tired of rebuilding proposals from scratch.",
  ],
  included=["Proposals pipeline (board, all, open proposals, win rate) + Follow up now list", "Services library with 3 tiers", "Fully written example proposal", "Proof & case studies bank", "Follow-up scripts", "7-step proposal guide", "Example data so you see how it works", "Quick-Start PDF guide"],
  specs=[("Currency", "Any — prices are plain numbers")],
  faq=[("Can I send the proposal to my client from Notion?", "Yes. Share the proposal page as a read-only link, or export it as a PDF.")],
),
"second-brain": dict(
  gid="gid://shopify/Product/16246052323677",
  title="Second Brain — Notion PARA Template for Notes, Ideas, Projects & SOPs",
  seo_title="Second Brain — Notion PARA Notes Template | Templyworks",
  seo_desc="Notion second brain built on PARA: inbox, projects, areas, ideas vault, SOPs and a 15-minute weekly review. Capture fast, find anything. Works on free Notion.",
  intro="Capture fast. Find anything. Second Brain is a calm PARA system in Notion for your notes, ideas, projects and processes — simple enough that you'll actually keep it.",
  bullets=[
    ("CAPTURE IN 5 SECONDS", "Type a title into the Inbox and you're done. The date saves itself. Sort it later."),
    ("BUILT ON PARA", "Projects, Areas, Resources, Archive — the proven method, already set up. Every note links to where it belongs."),
    ("IDEAS VAULT", "Business, content and side-project ideas tracked from Raw to Developing to Ready, so good ideas don't get buried."),
    ("SOPs INCLUDED", "Document any process you repeat. Three ready-made SOPs show you how."),
    ("15-MINUTE WEEKLY REVIEW", "A short Sunday checklist that clears the inbox and keeps the whole system alive."),
    ("PHONE + DESKTOP", "Capture on your phone, file on your laptop. Runs on Notion's free plan."),
  ],
  desc=[
    "Notes in five apps, ideas in your camera roll, processes in your head. Second Brain gives all of it one home — without a 40-page setup.",
    "The rule is simple: capture with just a title, file it on Sunday. That's the whole system.",
    "Built for freelancers, creators and students who want a second brain that stays tidy.",
  ],
  included=["Inbox with PARA filing", "Projects database", "Areas database", "Ideas vault", "SOPs (3 ready-made)", "Weekly review checklist", "Example data so you see how it works", "Quick-Start PDF guide"],
  specs=[],
  faq=[("I've never used PARA. Is that a problem?", "No. The template explains it in one short section, and the Quick-Start guide walks you through your first week.")],
),
"client-portal": dict(
  gid="gid://shopify/Product/16246058058077",
  title="Client Portal — Notion Client Dashboard for Freelancers (Milestones, Files, Feedback, Invoices)",
  seo_title="Client Portal — Notion Client Template | Templyworks",
  seo_desc="Shareable Notion client portal: milestones timeline, deliverables, feedback form, meeting notes and invoices in one link. End email chaos. Works on free Notion.",
  intro="One link. Zero email chaos. Client Portal is a shareable Notion page for each client, with milestones, deliverables, feedback and invoices in one place.",
  bullets=[
    ("ONE LINK PER CLIENT", "Duplicate the portal for each client and share it. They see what's next — you look professional."),
    ("MILESTONES ON A TIMELINE", "The whole project journey, phase by phase, in a view your client understands."),
    ("DELIVERABLES READY FOR REVIEW", "Every file with its status and version, so clients always find the latest one."),
    ("FEEDBACK IN ONE PLACE", "A built-in feedback form and a blockers list replace long email threads."),
    ("MEETING NOTES & INVOICES", "Every call summarised, every invoice with amount, due date and paid status."),
    ("USE IT WITH ALL YOUR CLIENTS", "Your licence lets you share your copies with your own clients. Runs on Notion's free plan."),
  ],
  desc=[
    "\"Can you resend that file?\" \"Where are we on this?\" \"Did you get my feedback?\" — Client Portal answers these before they're asked.",
    "Fill in the project-at-a-glance header, add milestones and share the page with your client. They can see progress, review files and leave feedback any time.",
    "Built for designers, developers, marketers and any freelancer who works with clients on projects.",
  ],
  included=["Project-at-a-glance header", "Milestones timeline", "Deliverables board", "Feedback & blockers + feedback form", "Meeting notes", "Invoice tracker", "Example data so you see how it works", "Quick-Start PDF guide + setup checklist inside the template"],
  specs=[("Licence", "Use with unlimited clients of your own (Notion Free allows up to 10 guests at a time; Plus removes the limit)")],
  faq=[("Can my clients edit it?", "You choose. Share it read-only, allow comments, or let them edit — it's a normal Notion share setting."),
       ("Am I allowed to share it with clients?", "Yes. You may duplicate the portal and share your copies with your own clients to deliver your services. You may not resell or publish the template itself. See our <a href=\"/pages/terms-of-service\">Terms of Service</a>.")],
),
"student-os": dict(
  gid="gid://shopify/Product/16456472691037",
  title="Student OS — Notion Student Planner (Grades, GPA, Assignments & Exams)",
  handle="student-os-notion-student-planner",
  tags=["notion", "productivity", "students", "study", "student-planner", "templyworks"],
  seo_title="Student OS — Notion Student Planner with GPA | Templyworks",
  seo_desc="Notion student planner: classes, assignments, exams, grades and automatic GPA in one system. For high school and college. Works on free Notion.",
  intro="Your school year, under control. Student OS keeps your classes, assignments, exams, grades and GPA in one Notion system — for high school and college.",
  bullets=[
    ("YOUR GPA, CALCULATED", "Enter a score and your weighted course grade, letter grade, GPA points and 'on track' status update instantly."),
    ("NEVER MISS A DEADLINE", "Every assignment with a live countdown that turns red when it's late. Table, board and calendar views."),
    ("EXAMS WITH A REVISION PLAN", "Every test with a countdown and a spaced revision plan, so you start early instead of cramming."),
    ("THIS WEEK AT A GLANCE", "What's due, what's next and how much you studied — on one page."),
    ("STUDY SESSIONS", "Log study time and see how much each class really gets."),
    ("ANY SCHOOL SYSTEM", "Uses a 4.0 GPA and percentages, and every scale is editable. Runs on Notion's free plan."),
  ],
  desc=[
    "Assignments in one app, grades in another, exam dates on a sticky note. Student OS puts your whole school year in one place and does the grade math for you.",
    "Routine: check <strong>This week</strong> every morning, add assignments the day you get them, and log a grade the day it comes back. Ten minutes on Sunday plans the week.",
    "Built for high school and college students who want structure without building a system from scratch.",
  ],
  included=["Courses with grade & GPA", "Assignments (table, board, calendar)", "Exams with revision plan", "Grades", "Study sessions", "Class schedule", "Notes & habit tracker", "Example data so you see how it works", "Quick-Start PDF guide + setup checklist inside the template"],
  specs=[("Grading", "GPA (4.0) and % — edit for any school system")],
  faq=[("I'm not in the US. Does it work for me?", "Yes. The grade scale is editable, so you can switch to your own system (points, 1–6, 1–15, percentages and so on).")],
),
}

def esc(s):
    return s  # copy is trusted, may contain simple HTML

def build(p):
    h = [f"<p><strong>{p['intro']}</strong></p>", "<h3>About this item</h3>", "<ul>"]
    h += [f"<li><strong>{a}</strong> — {b}</li>" for a, b in p["bullets"]]
    h += ["</ul>", "<h3>Product description</h3>"]
    h += [f"<p>{x}</p>" for x in p["desc"]]
    h += ["<h3>What's included</h3>", "<ul>"] + [f"<li>{x}</li>" for x in p["included"]] + ["</ul>"]
    specs = COMMON_SPECS[:4] + p["specs"] + COMMON_SPECS[4:]
    h += ["<h3>Specifications</h3>", "<table><tbody>"]
    h += [f"<tr><td><strong>{a}</strong></td><td>{b}</td></tr>" for a, b in specs]
    h += ["</tbody></table>", "<h3>Frequently asked questions</h3>"]
    own = {q for q, _ in p["faq"]}
    for q, a in p["faq"] + [f for f in COMMON_FAQ if f[0] not in own]:
        h.append(f"<p><strong>{q}</strong><br>{a}</p>")
    return "".join(h)

if __name__ == "__main__":
    out = {k: dict(v, html=build(v)) for k, v in P.items()}
    json.dump(out, open("descriptions.json", "w"), indent=1, ensure_ascii=False)
    for k, v in out.items():
        print(k, len(v["html"]), len(v["seo_desc"]), len(v["seo_title"]))
