"""Guide content for each Templyworks template. Matches the Notion templates as of Oct 2026."""

COMMON_START = [
    ("Duplicate the template", "Open the template link from your delivery email. Click the ··· menu (top right) and choose <b>Duplicate</b> / <b>Duplicate to my workspace</b>. Work only in your copy."),
    ("Clear or keep the examples", "Every database ships with a few example rows so you can see how things connect. Look through them, then delete them (select rows → Delete) or overwrite them with your own data."),
    ("Favourite the page", "Click the star (☆) at the top so the template sits in your sidebar. On mobile, it then appears under Favourites."),
]

COMMON_FAQ = [
    ("Which Notion plan do I need?", "The free plan runs everything essential. Some view types (e.g. Charts) have limits on free plans; all core databases and formulas work without upgrading."),
    ("Can I rename or add properties?", "Yes. If you rename a property that a formula or rollup uses, Notion updates the reference automatically. Deleting such a property breaks the formula that depends on it."),
    ("What currency is used?", "Amounts are plain numbers, so any currency works. If you want a symbol, open the property → Number format → pick your currency."),
    ("Something isn't working?", "Email info@templyworks.com with a screenshot. We fix setup problems quickly."),
]

TEMPLATES = [
    {
        "slug": "finance-hq",
        "name": "Finance HQ",
        "tagline": "Personal finance, calmly.",
        "intro": "Track income and spending, keep budgets in check automatically, save toward goals and keep every subscription in view.",
        "inside": [
            ("Transactions", "Every income and expense, one row each."),
            ("Budgets", "Monthly limit per category — spending fills in automatically."),
            ("Goals", "Savings targets with live progress."),
            ("Subscriptions", "Recurring costs with a monthly equivalent."),
            ("Visual Analytics", "Income, expenses and net for this month, last month and two months ago."),
        ],
        "setup": [
            ("Create your budgets", "In <b>Budgets</b>, add one row per spending category (e.g. Groceries, Dining, Transport) and enter a <b>Monthly Limit</b>."),
            ("Log your first transactions", "In <b>Transactions</b>, add a row with name, <b>Amount</b> (always positive), <b>Type</b> (Income or Expense), <b>Category</b> and <b>Date</b>."),
            ("Link expenses to a budget", "For each expense, set the <b>Budget</b> relation to the matching budget row. That is what feeds the budget's <b>Spent</b> number."),
            ("Add goals and subscriptions", "Enter <b>Target</b> and <b>Current</b> for each goal; enter <b>Amount</b> and <b>Billing Cycle</b> for each subscription."),
        ],
        "sections": [
            ("Transactions", [
                "<b>Amount</b> is always a positive number. <b>Type</b> decides whether it counts as money in or out.",
                "<b>Signed Amount</b> turns expenses negative automatically — this powers the Net figure in Visual Analytics.",
                "<b>This Month Spend</b> shows the amount only if the row is an expense dated this calendar month. Budgets add these up.",
                "Use the <b>New</b> button on mobile for quick entry — logging a purchase takes under 10 seconds.",
            ]),
            ("Budgets (automatic)", [
                "<b>Spent</b> = sum of linked expenses dated in the current month. It resets by itself when a new month starts.",
                "<b>Remaining</b> = Monthly Limit − Spent. <b>Used %</b> shows how much of the limit is gone.",
                "<b>Status</b>: 🟢 Healthy under 80%, 🟡 Watch from 80%, 🔴 Over above 100%.",
                "Only expenses linked via the <b>Budget</b> relation are counted. Income never counts toward a budget.",
            ]),
            ("Goals", [
                "Update <b>Current</b> whenever you save money toward a goal. <b>Progress %</b> calculates itself.",
                "Add a <b>Deadline</b> to keep the goal time-bound.",
            ]),
            ("Subscriptions", [
                "<b>Monthly Equivalent</b> converts yearly plans into a monthly cost, so you can compare everything fairly.",
                "Untick <b>Active</b> when you cancel — keep the row as a record.",
                "Keep <b>Next Payment</b> current so nothing surprises you.",
            ]),
            ("Visual Analytics", [
                "Three tabs: This Month, Last Month, 2 Months Ago — each with Income, Expenses, Net and an Income vs Expense chart.",
                "Everything is calculated from Transactions; there is nothing to fill in here.",
            ]),
        ],
        "routine": [
            ("Daily (1 min)", "Log what you spent today."),
            ("Weekly (5 min)", "Check budget Status. Anything 🟡 or 🔴? Adjust spending for the rest of the month."),
            ("Monthly (10 min)", "Review Visual Analytics, update goal balances, check Subscriptions for anything to cancel."),
        ],
        "tips": [
            "Name transactions consistently (\"Groceries — Edeka\") so search and filters stay useful.",
            "Create a budget called \"Other\" so no expense goes untracked.",
            "Not financial advice — the template organises your numbers, decisions stay yours.",
        ],
    },
    {
        "slug": "client-pipeline",
        "name": "Client Pipeline",
        "tagline": "A freelancer-friendly CRM.",
        "intro": "Contacts, deals, calls, emails and follow-ups in one place — so a warm lead never goes cold again.",
        "inside": [
            ("Contacts", "Every lead and client, with live pipeline value and last-contact date."),
            ("Deal Pipeline", "Opportunities moving from Prospect to Closed Won."),
            ("Interaction Log", "Every call, email, meeting and message — with follow-up flags."),
            ("Projects", "Work you're delivering, linked to the client."),
        ],
        "setup": [
            ("Add your contacts", "In <b>Contacts</b>, add a row per person with <b>Company</b>, <b>Email</b>, <b>Status</b> (Lead / Active / Inactive) and <b>Source</b>."),
            ("Create deals", "In <b>Deals</b>, add one row per opportunity, set <b>Value</b>, <b>Expected Close</b>, <b>Stage</b> and link the <b>Contact</b>."),
            ("Log your last touchpoints", "In <b>Interaction Log</b>, add your most recent call/email per contact, link the <b>Contact</b> and set a <b>Follow-up Date</b>."),
            ("Link active work", "When a deal closes, add a row in <b>Projects</b> and link the <b>Contact</b>."),
        ],
        "sections": [
            ("Contacts (automatic)", [
                "<b>Last Contacted</b> fills in automatically from the newest linked interaction — no manual date updates.",
                "<b>Pipeline Value</b> adds up the Value of every deal linked to this contact.",
                "Open any contact to see its <b>Deals</b>, <b>Interactions</b> and <b>Projects</b> in one place.",
            ]),
            ("Deal Pipeline", [
                "Stages: Prospect → Contacted → Proposal Sent → Negotiating → Closed Won / Closed Lost.",
                "Drag cards across the board view to move a deal forward.",
                "Keep <b>Expected Close</b> realistic — it is what you plan income around.",
            ]),
            ("Interaction Log", [
                "Set <b>Type</b> (Call, Email, Meeting, Message, Note) and write short <b>Notes</b>.",
                "<b>Follow-up Status</b> calculates itself: 🔴 Overdue, 🟡 Today, 🟢 Upcoming.",
                "Tick <b>Follow-up Done</b> when you've followed up — the flag disappears.",
            ]),
            ("Projects", [
                "Track <b>Start Date</b>, <b>Due Date</b>, <b>Budget</b> and <b>Status</b>.",
                "Linked projects appear on the contact's page automatically.",
            ]),
        ],
        "routine": [
            ("Daily (2 min)", "Filter Interaction Log for 🔴 Overdue and 🟡 Today. Send those follow-ups first."),
            ("After every call/email", "Log it in Interaction Log and set the next Follow-up Date."),
            ("Weekly (10 min)", "Move deal stages, update Expected Close, check contacts with an old Last Contacted date."),
        ],
        "tips": [
            "Always set a Follow-up Date — a lead without a next step is a lead you'll forget.",
            "Use Source to see where your best clients come from, then double down there.",
            "Mark lost deals Closed Lost instead of deleting them — patterns show up over time.",
        ],
    },
    {
        "slug": "project-tracker",
        "name": "Project Tracker",
        "tagline": "Run every project like a senior PM.",
        "intro": "Projects, tasks and time in one system — progress, health and billable totals calculate themselves.",
        "inside": [
            ("Projects", "Every engagement with automatic Progress, Health and hours."),
            ("Tasks", "Work broken into phases, with overdue flags."),
            ("Time Log", "Every hour you work, billable or not, with amounts."),
        ],
        "setup": [
            ("Create a project", "In <b>Projects</b>, add the project with <b>Client</b>, <b>Phase</b>, <b>Start Date</b>, <b>Due Date</b> and <b>Quoted Hours</b>."),
            ("Break it into tasks", "In <b>Tasks</b>, add tasks, link each to the <b>Project</b>, and set <b>Phase</b>, <b>Due Date</b>, <b>Priority</b> and <b>Est. Hours</b>."),
            ("Log your time", "In <b>Time Log</b>, add an entry per work session with <b>Hours</b>, <b>Date</b>, <b>Project</b>, <b>Rate</b> and whether it's <b>Billable</b>."),
        ],
        "sections": [
            ("Projects (automatic)", [
                "<b>Progress</b> = share of linked tasks marked Done.",
                "<b>Logged Hours</b> = sum of Time Log hours for the project. Compare with <b>Quoted Hours</b> to protect your budget.",
                "<b>Billable Total</b> = sum of billable time entry amounts.",
                "<b>Health</b>: ✅ Done when Completed · 🔴 Overdue after the due date · 🟡 At Risk when hours exceed the quote or the deadline is within 7 days and progress is under 75% · 🟢 On Track otherwise.",
            ]),
            ("Tasks", [
                "Phases: Discovery → Design → Review → Delivery.",
                "<b>Overdue</b> flags any task whose due date has passed and isn't Done.",
                "Views: <b>By Phase</b> kanban for daily work, <b>Due This Week</b> for focus.",
            ]),
            ("Time Log", [
                "<b>Amount</b> = Hours × Rate, only when Billable is ticked.",
                "Log time the same day — memory gets expensive by Friday.",
            ]),
            ("Views", [
                "<b>By Status</b> board: projects grouped by Not Started / In Progress / Completed, with Health and Progress on each card.",
                "<b>Timeline</b>: start-to-due bars for deadline planning.",
                "<b>By Client</b>: table sorted by client with all numbers.",
            ]),
        ],
        "routine": [
            ("Daily (2 min)", "Open Due This Week, pick today's tasks, log time when you finish."),
            ("Weekly (10 min)", "Scan project Health. Any 🟡 or 🔴 — talk to the client early, not late."),
            ("At project end", "Set Status to Completed, compare Logged vs Quoted Hours, use it to price the next job."),
        ],
        "tips": [
            "Quote in hours first, then price — the Logged vs Quoted comparison will teach you your real speed.",
            "Log non-billable time too (admin, revisions) so you see where time really goes.",
        ],
    },
    {
        "slug": "pitch-kit",
        "name": "Pitch Kit",
        "tagline": "Send proposals that close.",
        "intro": "A reusable services library, Good / Better / Best pricing and a follow-up system that turns \"I'll think about it\" into a signature.",
        "inside": [
            ("Proposals", "Every proposal from Draft to Accepted, with follow-up flags."),
            ("Services Library", "Your packages, built once, reused in every proposal."),
            ("Proposal Page Structure", "The 7-part flow every proposal follows."),
        ],
        "setup": [
            ("Build your Services Library", "Add your offers with <b>Tier</b> (Good / Better / Best), <b>Price</b>, <b>Est. Hours</b>, <b>Description</b> and <b>Deliverables</b>."),
            ("Create a proposal", "In <b>Proposals</b>, add a row with <b>Client Name</b>, set <b>Status</b> to Draft and link the offered packages under <b>Services</b>."),
            ("Write the proposal page", "Open the proposal row and write it using the 7-part structure below."),
            ("Send and set a follow-up", "Set <b>Status</b> to Sent, fill <b>Date Sent</b> and a <b>Follow-up Date</b> (2–4 days later)."),
        ],
        "sections": [
            ("Proposals (automatic)", [
                "<b>Package Price</b> adds up the Price of all linked services.",
                "<b>Deal Value</b> is what the client actually agreed to — fill it in when they accept.",
                "<b>Follow-up Status</b>: 🔴 Overdue, 🟡 Today, 🟢 Upcoming — only for proposals still open (not Draft, Accepted or Rejected).",
                "Status flow: Draft → Sent → Viewed → Accepted / Rejected.",
                "Use <b>Objections &amp; Notes</b> to record what the client pushed back on.",
            ]),
            ("Proposal page structure", [
                "<b>1. Problem</b> — their situation in their own words.",
                "<b>2. Solution</b> — your approach, outcomes before process.",
                "<b>3. Why Me</b> — one or two relevant proof points.",
                "<b>4. Deliverables</b> — exactly what they get. Vague scope causes scope creep.",
                "<b>5. Timeline</b> — realistic phases and dates.",
                "<b>6. Pricing</b> — three tiers. Most clients pick the middle; anchor high.",
                "<b>7. Next Steps</b> — one clear action, e.g. \"Reply to confirm and I'll send the contract.\"",
            ]),
            ("Services Library", [
                "Open any service to see every proposal it was used in.",
                "Review prices every quarter — raise them on the tier clients pick most.",
            ]),
        ],
        "routine": [
            ("Per proposal", "Draft from the structure, link services, send, set a follow-up date."),
            ("Daily (1 min)", "Check 🔴 Overdue / 🟡 Today follow-ups and nudge."),
            ("Monthly", "Count Accepted vs Rejected, read your Objections notes, adjust offers."),
        ],
        "tips": [
            "Send within 24 hours of the call while interest is high.",
            "Follow up at least twice — most yeses come after the first nudge.",
        ],
    },
    {
        "slug": "second-brain",
        "name": "Second Brain",
        "tagline": "Your second brain — finally organised.",
        "intro": "Capture anything fast, sort it with the PARA method, keep ideas separate and document the processes you repeat.",
        "inside": [
            ("Inbox", "The lowest-friction place to capture anything."),
            ("Ideas Vault", "Business, template, content and product ideas."),
            ("SOPs", "Step-by-step processes you repeat."),
            ("PARA Reference", "Projects, Areas, Resources, Archive explained."),
        ],
        "setup": [
            ("Capture five things", "Add five items to <b>Inbox</b> right now — articles, notes, tasks, anything. Just a title is enough."),
            ("Do your first sort", "For each item set <b>PARA</b>, add <b>Tags</b> and a one-line <b>My Summary</b>, then tick <b>Filed</b>."),
            ("Move ideas over", "Anything that is an idea rather than a note goes into <b>Ideas Vault</b> with Status Raw."),
            ("Write one SOP", "Pick a task you do often (e.g. invoicing) and write its steps in a new <b>SOPs</b> page."),
        ],
        "sections": [
            ("Inbox", [
                "<b>Date Saved</b> fills in automatically when you create an entry.",
                "Capture first, organise later. Speed beats structure at capture time.",
                "Tick <b>Review This</b> for items you want to revisit; tick <b>Filed</b> once sorted — it leaves the Inbox view.",
            ]),
            ("PARA method", [
                "<b>Projects</b> — has a deadline and an outcome (e.g. client website, launch).",
                "<b>Areas</b> — ongoing responsibility with no end date (Finance, Health, Marketing).",
                "<b>Resources</b> — reference material by topic you want to find later.",
                "<b>Archive</b> — finished or inactive. Move here, don't delete.",
            ]),
            ("Ideas Vault", [
                "<b>Date Captured</b> fills in automatically.",
                "Status: Raw → Developing → Ready, or Shelved when it's not for now.",
            ]),
            ("SOPs", [
                "<b>Last Updated</b> changes automatically whenever you edit an SOP.",
                "Set <b>Owner / Delegate To</b> once someone else can run the process.",
                "Mark <b>Needs Update</b> when a process changed but the page didn't yet.",
            ]),
        ],
        "routine": [
            ("Anytime", "Capture into Inbox — phone or desktop."),
            ("Weekly review (15 min)", "Open Inbox (not Filed). Give each item PARA, Tags and a summary, tick Filed. Skim Ideas Vault and move anything exciting from Raw to Developing."),
            ("Monthly", "Archive finished projects, review SOPs marked Needs Update."),
        ],
        "tips": [
            "Write My Summary in your own words — that is what makes notes useful later.",
            "Any process you repeat more than three times deserves an SOP.",
        ],
    },
    {
        "slug": "client-portal",
        "name": "Client Portal",
        "tagline": "The client-facing hub that ends email chaos.",
        "intro": "Milestones, deliverables, feedback, meetings and invoices on one shareable page your client can open anytime.",
        "inside": [
            ("Milestones", "The project journey, phase by phase."),
            ("Deliverables", "Every file by version: v1, v2, Final."),
            ("Feedback & Blockers", "Client feedback and anything blocking progress."),
            ("Meeting Notes", "Every call summarised, in date order."),
            ("Invoices", "Amounts, due dates and automatic payment status."),
            ("FAQ", "Client-facing answers on revisions, payments and contact."),
        ],
        "setup": [
            ("One portal per client", "Duplicate the whole portal page once for each client and rename it (e.g. \"Aurora Studios — Portal\")."),
            ("Fill in your details", "Edit the FAQ: replace <b>your@email.com</b> with your own email and adjust revisions and payment terms to your contract."),
            ("Set up the project", "Add Milestones with Phase and Due Date, and your first Invoice with Amount and Due Date."),
            ("Share with the client", "Click <b>Share</b> → invite your client by email. Give <b>Can comment</b> or <b>Can edit</b> access so they can add feedback."),
        ],
        "sections": [
            ("Milestones & Deliverables", [
                "Milestone <b>Status</b>: Upcoming → In Progress → Done.",
                "Each deliverable gets a <b>Version</b> (v1, v2, Final), a <b>File Link</b> and a <b>Status</b> (In Progress, Ready for Review, Approved).",
            ]),
            ("Feedback & Blockers", [
                "Clients add feedback directly as a row — no email threads.",
                "<b>Type</b> \"Waiting on Client\" + the <b>Waiting on You</b> view shows the client exactly what's blocking progress.",
                "Set Status to Resolved once handled.",
            ]),
            ("Invoices (automatic)", [
                "<b>Status</b> calculates itself: ✅ Paid once <b>Paid Date</b> is filled, 🔴 Overdue after the Due Date, otherwise 🟡 Pending.",
                "Just enter the Paid Date when money arrives — no manual status changes.",
            ]),
            ("Before you share", [
                "Delete the example rows and replace the FAQ email.",
                "Check sharing: only invite the client — don't publish the page to the web unless you want it public.",
                "The licence toggle at the bottom is for you; clients can ignore it.",
            ]),
        ],
        "routine": [
            ("After every call", "Add a Meeting Notes row with Summary and Action Items."),
            ("When you deliver", "Add or update the Deliverable, set Ready for Review, tell the client in one line."),
            ("Weekly", "Update milestone Status, resolve feedback, check invoice Status."),
        ],
        "tips": [
            "Send the portal link on day one — clients judge your organisation early.",
            "Keep all feedback in the portal; politely redirect emailed feedback there.",
        ],
    },
    {
        "slug": "custom-template",
        "kind": "service",
        "name": "Custom Template",
        "tagline": "Your personal Notion system — built for you.",
        "cover_label": "YOUR CUSTOM BUILD GUIDE",
        "intro": "Thanks for ordering a Custom Template. We design a Notion workspace from scratch around how you work. This guide explains what happens next, how to write a great brief, and how to use your finished system.",
        "inside": [
            ("Your workspace", "A personal Notion system designed around your brief."),
            ("Delivery", "Private Notion link within 3–5 business days after your complete brief."),
            ("Revision", "One round of changes included."),
            ("Notion plan", "Built to work on a free Notion account."),
            ("Support", "Questions answered by email at info@templyworks.com."),
        ],
        "setup_title": "How it works",
        "page2_title": "Your brief & next steps",
        "callout": "<b>Start now:</b> reply to our email with your brief (questions on the next page). Delivery time starts once your brief is complete.",
        "setup": [
            ("Order confirmed", "You receive an order confirmation right away."),
            ("Send your brief", "Reply to our email with your answers to the brief questions on the next page. The clearer the brief, the better the result."),
            ("We design it", "We build your workspace. If something is unclear we ask — the clock starts once the brief is complete."),
            ("You receive your link", "Within 3–5 business days you get a private Notion link. Open it and click Duplicate to copy it into your workspace."),
            ("One revision round", "Try it for a few days, then send all change requests in one email. We update the system and send the new link."),
        ],
        "sections": [
            ("Your brief — answer these", [
                "<b>Who are you?</b> Job, business or study — and how many people will use the workspace.",
                "<b>What should it solve?</b> The 1–3 problems that frustrate you most today.",
                "<b>What do you track?</b> E.g. clients, projects, tasks, money, content, habits, notes.",
                "<b>Your routine:</b> what you do daily, weekly and monthly — and on which device.",
                "<b>What didn't work before?</b> Templates or tools you tried and why they failed.",
                "<b>Must-haves vs nice-to-haves:</b> list them separately.",
                "<b>Style:</b> minimal or visual, light or dark, language (English or German).",
                "<b>Examples:</b> screenshots or links of setups you like (optional, very helpful).",
            ]),
            ("Tips for a great brief", [
                "Describe your real workflow, not your ideal one — we build for how you actually work.",
                "Fewer, clearer goals beat a long wish list. You can always grow the system later.",
                "Mention anything time-sensitive (deadlines, launch dates).",
            ]),
            ("Your revision round", [
                "Use the system for a few days before sending changes — real use shows what matters.",
                "Send all changes in <b>one</b> email so nothing gets lost.",
                "Revisions cover adjustments to the agreed scope (fields, views, layout, wording). Completely new features or a different scope can be quoted separately.",
            ]),
            ("After delivery", [
                "Duplicate the link into your workspace, then delete or overwrite the example entries.",
                "Fields with formulas or rollups fill in by themselves — you never type into them.",
                "Favourite the main page (☆) so it sits in your sidebar and on mobile.",
            ]),
        ],
        "routine_title": "Timeline",
        "routine": [
            ("Day 0", "Order + send your brief."),
            ("Day 1–5 (business days)", "We build. Delivery by email with your private Notion link."),
            ("After delivery", "Test it, then send your revision request in one email."),
            ("Revision", "Updated link, usually within 2 business days."),
        ],
        "tips": [
            "Reply to the order email if you can't find our brief request — check spam first.",
            "Keep the delivered link private; it's licensed for you (and your own clients' work), not for resale.",
        ],
        "faq": [
            ("When does the 3–5 days start?", "When we have your complete brief. If we need to ask questions, the time starts once they're answered."),
            ("Can I use it with my team?", "Yes — share your duplicated workspace with collaborators inside Notion."),
            ("Can you build something for a paid Notion feature?", "Tell us in the brief. By default everything works on the free plan."),
            ("Something isn't working?", "Email info@templyworks.com with a screenshot."),
        ],
        "licence": "Licence: personal and business use, including work for your own clients. Reselling or redistributing the workspace as a template is not allowed. Statutory rights remain unaffected.",
    },
    {
        "slug": "abitur-system",
        "lang": "de",
        "name": "Abitur-System",
        "file_name": "Abitur-System",
        "tagline": "Deine Kommandozentrale für die Oberstufe.",
        "intro": "Noten, Klausuren, Stundenplan, Aufgaben, Termine, Fehlzeiten und Gewohnheiten an einem ruhigen Ort — von der ersten Klausur bis zur Abi-Feier.",
        "inside": [
            ("Dashboard", "Ø Notenpunkte, offene Klausuren, offene Aufgaben und Fehlstunden auf einen Blick."),
            ("Stundenplan", "Deine Kurse nach Wochentag und Block, mit A/B-Wochen."),
            ("Tasks", "Hausaufgaben, Lernen, Referate — mit Fälligkeit und Priorität."),
            ("Habits", "Gewohnheiten mit Streak, z. B. täglich lernen oder Sport."),
            ("Noten", "Alle Leistungen Q1–Q4 mit automatischer Umrechnung Punkte → Note."),
            ("Klausuren", "Jede Klausur mit Countdown, Lernstart-Erinnerung und Lernfortschritt."),
            ("Termine", "Abgaben, Prüfungen, Facharbeit, Zeugnisse — mit Countdown."),
            ("Fehlzeiten", "Fehlstunden und ob die Entschuldigung abgegeben ist."),
        ],
        "setup": [
            ("Stundenplan eintragen", "Lege in <b>Stundenplan</b> pro Kursstunde eine Zeile an: <b>Kurs</b>, <b>Wochentag</b>, <b>Block</b>, <b>Raum</b>, <b>Lehrkraft</b>. Hast du A/B-Wochen, setze <b>Woche</b> auf A oder B, sonst „Beide“. Passe die Blockzeiten bei Bedarf an deine Schule an."),
            ("Klausuren anlegen", "Trage in <b>Klausuren</b> jede bekannte Klausur mit <b>Datum</b>, <b>Halbjahr</b> und <b>Themen</b> ein. Setze einen <b>Lernstart</b> — Notion erinnert dich an dem Tag automatisch."),
            ("Noten, Termine & Habits", "In <b>Noten</b>: <b>Punkte</b> (0–15), <b>Art</b>, <b>Halbjahr</b> und <b>Gewichtung</b> — die Note rechnet sich selbst aus. Wichtige Termine (Abgaben, Facharbeit, Abi-Prüfungen) in <b>Termine</b>; 2–4 Gewohnheiten in <b>Habits</b>."),
        ],
        "callout": "",
        "sections": [
            ("Noten (automatisch)", [
                "Felder mit Formel (Note, Tage bis Klausur, Countdown) füllen sich selbst — dort tippst du nie etwas ein. Bleibt eines leer, fehlt meist ein Datum oder eine Punktzahl.",
                "<b>Punkte</b> 0–15 eintragen — <b>Note</b> wird automatisch umgerechnet (z. B. 13 Punkte = 1−).",
                "<b>Gewichtung</b> bestimmt, wie stark eine Leistung zählt (z. B. Klausur 2, Mündlich 1). Daraus entstehen die <b>gewichteten Punkte</b> für deinen Schnitt.",
                "<b>Ø Notenpunkte</b> oben im Dashboard rechnet sich aus allen eingetragenen Noten.",
                "Filtere nach <b>Halbjahr</b> (Q1–Q4), um jedes Halbjahr einzeln zu sehen.",
            ]),
            ("Klausuren", [
                "<b>Tage bis Klausur</b> zählt automatisch runter. <b>Lernphase</b> zeigt dir, wie dringend es ist.",
                "<b>Lernstart</b> hat eine Erinnerung um 17:00 am gewählten Tag.",
                "Status: Noch nicht begonnen → Am Lernen → Wiederholung → Bereit → Geschrieben.",
                "Pflege <b>Lernfortschritt %</b> und <b>Lernzeit gesamt</b>, um ehrlich zu sehen, wo du stehst. Links zu Materialien gehören in <b>Materialien / Links</b>.",
                "Nach der Klausur: Status „Geschrieben“ und die Punkte in <b>Noten</b> eintragen.",
            ]),
            ("Tasks & Habits", [
                "<b>Fälligkeit</b> zeigt automatisch, was heute fällig oder überfällig ist.",
                "<b>Typ</b> (Aufgabe, Lernen, Lesen, Projekt, Referat) und <b>Priorität</b> helfen beim Sortieren.",
                "Habits: Hake <b>Heute</b> ab, wenn erledigt, und zähle deinen <b>Streak</b> hoch. Unten im Dashboard siehst du „Streak pro Bereich“ und „Heute erledigt“.",
            ]),
            ("Termine & Fehlzeiten", [
                "<b>Countdown</b> bei Terminen rechnet sich selbst; am Vortag um 18:00 kommt eine Erinnerung.",
                "Fehlzeiten: Datum, <b>Fehlstunden</b>, <b>Art</b> eintragen und <b>Entschuldigung abgegeben</b> abhaken — <b>Status</b> zeigt dir, was noch offen ist.",
            ]),
        ],
        "routine": [
            ("Täglich (2 Min.)", "Tasks abhaken, Habits „Heute“ setzen, kurz auf offene Klausuren schauen."),
            ("Nach jeder Note", "Punkte + Gewichtung in Noten eintragen — dein Schnitt ist sofort aktuell."),
            ("Wöchentlich (10 Min.)", "Neue Klausuren/Termine eintragen, Lernstart setzen, Fehlzeiten-Entschuldigungen prüfen."),
            ("Halbjahresende", "Halbjahr filtern, Schnitt prüfen, Ziele fürs nächste Halbjahr setzen."),
        ],
        "tips": [
            "Lege den Lernstart 10–14 Tage vor jeder Klausur — die Erinnerung macht den Rest.",
            "Trage auch mündliche Noten ein; sie zählen oft mehr, als man denkt.",
            "Die Umrechnung und Gewichtung kannst du an die Regeln deines Bundeslandes anpassen.",
            "Pinne das Dashboard als Favorit (☆) — so ist es auf dem Handy mit einem Tipp offen.",
        ],
        "faq": [
            ("Brauche ich Notion Plus?", "Nein. Alles Wichtige läuft im kostenlosen Notion-Plan. Notion Free erlaubt nur ein Diagramm — die Diagramme unten im Dashboard sehen mit Plus am vollständigsten aus."),
            ("Kann ich Kurse und Felder ändern?", "Ja, alles ist frei anpassbar. Benennst du ein Feld um, das eine Formel nutzt, passt Notion die Formel automatisch an."),
            ("Mein Bundesland zählt anders.", "Passe die Gewichtung pro Leistung an. Die Punkte-Skala 0–15 gilt bundesweit."),
            ("Etwas funktioniert nicht?", "Schreib an info@templyworks.com mit einem Screenshot."),
        ],
        "licence": "Lizenz: Nutzung für deine eigene Schulzeit und dein Privatleben. Weiterverkauf, Weitergabe oder Veröffentlichung des Templates ist nicht erlaubt. Digitales Produkt — alle Käufe sind nach der Bereitstellung endgültig (Zustimmung beim Kauf, § 356 Abs. 5 BGB). Gesetzliche Gewährleistungsrechte bleiben unberührt.",
    },
]

COMMON_START_DE = [
    ("Template duplizieren", "Öffne den Link aus deiner Bestell-E-Mail. Klicke oben rechts auf ··· und dann auf <b>Duplizieren</b>. Arbeite nur in deiner Kopie."),
    ("Beispiele löschen", "Jede Datenbank enthält ein paar Beispielzeilen. Schau sie dir an und lösche sie dann (Zeilen markieren → Löschen) oder überschreibe sie mit deinen Daten."),
    ("Als Favorit markieren", "Klicke oben auf den Stern (☆). So findest du das System in der Seitenleiste und am Handy unter Favoriten."),
]
