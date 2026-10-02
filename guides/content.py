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
]
