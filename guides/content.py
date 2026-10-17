"""Guide content for each Templyworks template. Matches the Notion templates as of Oct 2026."""

COMMON_START = [
    ("Duplicate the template", "Open the template link from your delivery email. Click the ··· menu (top right) and choose <b>Duplicate</b> / <b>Duplicate to my workspace</b>. Work only in your copy."),
    ("Clear or keep the examples", "Every database ships with a few example rows so you can see how things connect. Look through them, then delete them (select rows → Delete) or overwrite them with your own data."),
    ("Favourite the page", "Click the star (☆) at the top so the template sits in your sidebar. On mobile, it then appears under Favourites."),
]

COMMON_FAQ = [
    ("Which Notion plan do I need?", "The free plan. Every database, formula and view in this template works without upgrading."),
    ("Can I rename or add properties?", "Yes. If you rename a property that a formula or rollup uses, Notion updates the reference automatically. Deleting such a property breaks the formula that depends on it."),
    ("What currency is used?", "Amounts are plain numbers, so any currency works. If you want a symbol, open the property → Number format → pick your currency."),
    ("Something isn't working?", "Email info@templyworks.com with a screenshot. We fix setup problems quickly."),
]

TEMPLATES = [
    {
        "slug": "finance-hq",
        "name": "Finance HQ",
        "accent": "#48c480",
        "tagline": "Personal finance, calmly.",
        "intro": "Every transaction, budget, bill, goal and account in one place — with your net worth and monthly numbers calculated for you. No spreadsheet anxiety.",
        "inside": [
            ("At a glance", "Net worth, bills coming up and a budget check at the top of the page."),
            ("Transactions", "Every income and expense, one row each. Views: This Month, All, Expenses, Income."),
            ("Budgets", "A monthly limit per category — Spent, Remaining, Used % and Status update live."),
            ("Goals & Savings Pots", "Savings targets with live progress."),
            ("Accounts & Net Worth", "Every account and debt; net worth adds itself up."),
            ("Subscriptions & Bills", "Recurring payments with a monthly cost and next payment date."),
            ("This month in numbers", "Money in and money out for the current month, with totals."),
            ("Bonus (paid plans)", "Optional charts and a visual dashboard. Everything else works on the free plan."),
        ],
        "setup": [
            ("Create your budgets", "In <b>Budgets</b>, add one row per spending category (e.g. Groceries, Dining, Transport) and enter a <b>Monthly Limit</b>."),
            ("Add your accounts", "In <b>Accounts &amp; Net Worth</b>, add each bank account, savings pot, credit card and loan with its current balance. Cards and loans count as debt automatically."),
            ("Log your first transactions", "In <b>Transactions</b>, add name, <b>Amount</b> (always positive), <b>Type</b> (Income or Expense), <b>Category</b> and <b>Date</b>. For expenses, pick the matching <b>Budget</b>."),
            ("Add goals and bills", "Enter target and current amount for each goal; enter amount, billing cycle and next payment for each subscription or bill."),
        ],
        "sections": [
            ("Transactions", [
                "<b>Amount</b> is always a positive number. <b>Type</b> decides whether it counts as money in or out.",
                "Pick a <b>Budget</b> on every expense — that is what feeds the budget's <b>Spent</b> number.",
                "The <b>This Month</b> view only shows the current calendar month and switches over by itself.",
                "On mobile, add Finance HQ to Favourites — logging a coffee takes 10 seconds.",
            ]),
            ("Budgets (automatic)", [
                "<b>Spent</b> = linked expenses dated this month. It resets when a new month starts.",
                "<b>Remaining</b> = Monthly Limit − Spent. <b>Used %</b> shows how much of the limit is gone.",
                "<b>Status</b>: 🟢 Healthy, 🟡 Watch when you get close, 🔴 Over when you pass the limit.",
                "Income never counts toward a budget.",
            ]),
            ("Accounts & Net Worth", [
                "Update balances once a month. Credit cards and loans are counted as debt automatically.",
                "The <b>Net worth</b> table at the top of the page shows the total at the bottom of the column.",
            ]),
            ("Subscriptions & Bills", [
                "Yearly plans are converted to a monthly cost, so you see what you really pay.",
                "Click a <b>Next Payment</b> date → turn on <b>Remind</b> to get a notification before it's charged.",
            ]),
            ("This month in numbers", [
                "Money in and Money out list this month's transactions with the total at the bottom.",
                "Want last month? Open Transactions → All and filter by date.",
            ]),
        ],
        "routine": [
            ("When it happens (10 sec)", "Log a transaction."),
            ("Weekly (2 min)", "Check this page: budget status and bills coming up."),
            ("Monthly (5 min)", "Update account balances and goal amounts; check subscriptions for anything to cancel."),
        ],
        "tips": [
            "Freelancer? Each time a client pays, move 25–30% to a Tax reserve account and update the goal.",
            "Create a budget called \"Other\" so no expense goes untracked — and merge categories that don't change your decisions.",
            "Not financial advice — the template organises your numbers, decisions stay yours.",
        ],
        "faq": [
            ("Which Notion plan do I need?", "The free plan. Everything works free; only the optional charts in the Bonus toggle need a paid Notion plan."),
            ("Which currency does it use?", "Any. Amounts are plain numbers — use your own currency."),
            ("Does it connect to my bank?", "No. You add transactions yourself, so nothing is shared with anyone."),
            ("Something isn't working?", "Email info@templyworks.com with a screenshot. We fix setup problems quickly."),
        ],
    },
    {
        "slug": "client-pipeline",
        "name": "Client Pipeline",
        "accent": "#58aae6",
        "tagline": "A freelancer-friendly CRM.",
        "intro": "Leads, deals, calls and follow-ups in one place — so no warm lead ever goes cold because you forgot to reply.",
        "inside": [
            ("Today's focus", "Follow-ups due this week and your open deals, at the top of the page."),
            ("Deal Pipeline", "A board from Prospect to Closed Won — every deal with value and a next step."),
            ("Contacts", "Every lead and client. Last Contacted and Pipeline Value fill in by themselves."),
            ("Interaction Log", "Every call, email and meeting with a follow-up date."),
            ("Projects", "Work you're delivering for won deals, linked to the client."),
        ],
        "setup": [
            ("Add your contacts", "In <b>Contacts</b>, add a row per person with company, email, status and <b>Source</b> (where they came from)."),
            ("Create your deals", "In <b>Deals</b>, add one row per opportunity with <b>Value</b>, <b>Stage</b>, the linked contact and a <b>Next step</b>."),
            ("Log your last touchpoints", "In <b>Interaction Log</b>, add your most recent call or email per contact and set a <b>Follow-up Date</b>."),
        ],
        "sections": [
            ("Today's focus", [
                "Shows every follow-up due this week and the deals that are still open.",
                "Open the page in the morning, clear the list, done.",
            ]),
            ("Deal Pipeline", [
                "Drag cards across stages: Prospect → Contacted → Proposal Sent → Negotiating → Closed Won / Closed Lost.",
                "Always fill <b>Next step</b> — a deal without a next step is a deal you're losing.",
                "Mark lost deals Closed Lost instead of deleting them — patterns show up over time.",
            ]),
            ("Contacts (automatic)", [
                "<b>Last Contacted</b> comes from the newest linked interaction — no manual date updates.",
                "<b>Pipeline Value</b> adds up the value of every deal linked to the contact.",
                "Open a contact to see its deals, interactions and projects in one place.",
            ]),
            ("Interaction Log", [
                "One row per call, email, meeting or message, with short notes and a <b>Follow-up Date</b>.",
                "Tick <b>Follow-up Done</b> when you've replied — it leaves Today's focus.",
                "Click a Follow-up Date → turn on <b>Remind</b> to get a notification.",
            ]),
            ("Projects", [
                "Won a deal? Add the project with dates and budget and link the contact.",
            ]),
        ],
        "routine": [
            ("Every morning (5 min)", "Clear the follow-ups in Today's focus."),
            ("After every call or email (30 sec)", "Log it in the Interaction Log with the next follow-up date."),
            ("Weekly (10 min)", "Move deal stages and update every Next step."),
        ],
        "tips": [
            "Reply within 24 hours — fast replies convert far more often.",
            "Follow up twice: day 3 \"Did this land OK?\", day 7 \"Should I keep the slot open?\"",
            "Fill Source on every contact — after 3 months you'll know where your best clients come from.",
        ],
    },
    {
        "slug": "project-tracker",
        "name": "Project Tracker",
        "accent": "#ecc448",
        "tagline": "Run every project like a senior PM.",
        "intro": "Every deadline across every client, project health that calculates itself, quoted vs real hours — and a scope log so \"small extras\" finally get paid.",
        "inside": [
            ("This week", "Tasks due in the next 7 days and active projects, at the top of the page."),
            ("Projects", "One row per project. Health, Progress and Logged Hours calculate themselves."),
            ("Tasks", "Work broken into phases; anything late turns red automatically."),
            ("Scope Changes", "Extra requests with a price — approved fees roll up into the project."),
            ("Time Log", "Every hour you work, with rate and billable total."),
        ],
        "setup": [
            ("Create a project", "In <b>Projects</b>, add the project with client, start date, due date and <b>Quoted Hours</b>."),
            ("Break it into tasks", "In <b>Tasks</b>, add tasks, link each to the project, and set phase and due date."),
            ("Log your time", "In <b>Time Log</b>, add an entry per work session with hours, date, project and rate."),
        ],
        "sections": [
            ("Projects (automatic)", [
                "<b>Progress</b> = share of linked tasks that are done.",
                "<b>Logged Hours</b> adds up the Time Log. Compare it with <b>Quoted Hours</b> to protect your budget.",
                "<b>Health</b>: 🟢 On Track, 🟡 At Risk, 🔴 Overdue — from deadline, progress and hours.",
                "Views: board by status, <b>Timeline</b> for deadlines side by side, and by client.",
            ]),
            ("Tasks", [
                "Phases: Discovery → Design → Review → Delivery.",
                "Any task past its due date and not done is flagged automatically.",
                "Click a task's Due Date → turn on <b>Remind</b> to get a notification.",
            ]),
            ("Scope Changes", [
                "Client asks for \"one small extra\"? Log it, put a price on it, and only start when <b>Client said yes</b> is ticked.",
                "Approved fees roll up into the project automatically.",
            ]),
            ("Time Log", [
                "Log time the same day — memory gets expensive by Friday.",
                "Log non-billable time too (admin, revisions) to see where time really goes.",
            ]),
        ],
        "routine": [
            ("Every morning (2 min)", "Open This week and pick today's tasks."),
            ("As you work", "Tick tasks as you finish them — progress and health update by themselves."),
            ("End of day (1 min)", "Log your hours."),
            ("At project end", "Compare Logged vs Quoted Hours and price the next job from it."),
        ],
        "tips": [
            "Never say \"sure, no problem\" to extras. Say \"Happy to — I'll send a quick quote\" and log it in Scope Changes.",
            "Retainer clients? Create the monthly tasks once, then duplicate them each month and change the dates.",
            "If Logged Hours beat Quoted Hours by 30%, quote 30% more next time.",
        ],
    },
    {
        "slug": "pitch-kit",
        "name": "Pitch Kit",
        "accent": "#be8cf5",
        "tagline": "Send proposals that close.",
        "intro": "A Good/Better/Best service library, a fully written example proposal, a proof bank of case studies and ready-to-send follow-up scripts that turn \"I'll think about it\" into a signature.",
        "inside": [
            ("Today's focus", "Proposals to follow up now and your scoreboard, at the top of the page."),
            ("Proposals", "Every proposal from Draft to Accepted. Open Aurora Studios for a fully written example."),
            ("Services Library", "Your Good / Better / Best packages, built once, linked to every proposal."),
            ("Proof & Case Studies", "Wins with problem, result and quote — your \"Why me\" ammo."),
            ("Follow-up Scripts", "Copy-and-send messages for every stage of the deal."),
            ("The 7-step proposal", "The flow every proposal follows, with what to write in each step."),
        ],
        "setup": [
            ("Build your Services Library", "Replace the example services with your own offers: <b>Tier</b> (Good / Better / Best), <b>Price</b>, hours and deliverables."),
            ("Add 1–3 case studies", "In <b>Proof &amp; Case Studies</b>, log past wins: problem → result → client quote."),
            ("Write your first proposal", "Duplicate the <b>Aurora Studios</b> proposal, rename it for your client, link the services you offer and rewrite each step."),
            ("Send and set a follow-up", "Set Status to Sent, fill the sent date and a <b>Follow-up Date</b> 2–4 days later."),
        ],
        "sections": [
            ("Proposals (automatic)", [
                "Status flow: Draft → Sent → Viewed → Accepted / Rejected.",
                "The package price adds up from the linked services by itself.",
                "<b>Follow up now</b> lists every open proposal whose follow-up date has come.",
                "The optional Win Rate chart tab uses Notion's 1 free chart — skip it if you've already used yours.",
            ]),
            ("The 7-step proposal", [
                "<b>1. Problem</b> — their situation in their own words.",
                "<b>2. Solution</b> — your approach; outcomes before process.",
                "<b>3. Why me</b> — one or two case studies from your Proof bank.",
                "<b>4. Deliverables</b> — exactly what they get. Vague scope causes scope creep.",
                "<b>5. Timeline</b> — realistic phases and dates.",
                "<b>6. Pricing</b> — a Good / Better / Best table. Most clients pick the middle.",
                "<b>7. Next step</b> — one clear action, e.g. \"Reply 'Better' and I'll send the contract today.\"",
            ]),
            ("Follow-up Scripts", [
                "One message per stage: after the call, proposal sent, day-3 nudge, day-7 check-in, objections, lost, won.",
                "Copy, personalise the first line, send.",
            ]),
        ],
        "routine": [
            ("New lead", "Send the proposal within 24 hours, while interest is highest."),
            ("Every morning (1 min)", "Check Follow up now and nudge with a script."),
            ("Monthly", "Look at Accepted vs Rejected and adjust your packages and prices."),
        ],
        "tips": [
            "Personalise the first paragraph with their words from the call. Template everything else.",
            "Follow up at least twice — most yeses come after a nudge.",
            "Click a Follow-up Date → turn on Remind so you never forget.",
        ],
    },
    {
        "slug": "second-brain",
        "name": "Second Brain",
        "accent": "#f08cb9",
        "tagline": "Your second brain — finally organised.",
        "intro": "Capture anything in seconds, file it later, and find it again when you need it. Built on PARA (Projects, Areas, Resources, Archive) — without the overwhelm.",
        "inside": [
            ("Right now", "Unfiled Inbox items and active projects, at the top of the page."),
            ("Inbox", "Capture with just a title. File it later."),
            ("Projects", "Anything with a deadline and an outcome, with every linked note."),
            ("Areas", "Ongoing responsibilities (Clients, Money, Health…) with their projects and notes."),
            ("Ideas Vault", "Business, product and content ideas from Raw to Ready."),
            ("SOPs", "Processes you repeat, written down once — three examples included."),
            ("Weekly Review", "A 15-minute Sunday checklist that keeps the system alive."),
        ],
        "setup": [
            ("Set up your Areas", "Replace the example Areas with your 5–10 ongoing responsibilities."),
            ("Add your current projects", "In <b>Projects</b>, add what you're working on now and link each to an Area."),
            ("Capture five things", "Type five titles into the <b>Inbox</b> — articles, notes, ideas. Nothing else needed."),
        ],
        "sections": [
            ("Inbox", [
                "Only the title is required; the date saves itself.",
                "When you process an item, link it to a <b>Project</b> or <b>Area</b>, or set PARA to Resources / Archive, then tick <b>Filed</b>.",
                "Not sure where it goes? Leave it. Filing is optional — capturing is not.",
            ]),
            ("Where does a note go? (10-second rule)", [
                "Helps a project with a deadline → link it to that <b>Project</b>.",
                "About an ongoing responsibility → link it to that <b>Area</b>.",
                "Might be useful someday → PARA = <b>Resources</b>.",
                "None of the above → <b>Archive</b>. You can always search for it.",
            ]),
            ("Ideas Vault & SOPs", [
                "Ideas stay apart from notes so they don't get buried. Move them Raw → Developing → Ready.",
                "Do something 3 times? Write an SOP once — ready to reuse or hand off.",
            ]),
            ("Weekly Review", [
                "Open the example week for the checklist and duplicate it each Sunday.",
                "Clear the Inbox, check projects, pick next week's focus. 15 minutes.",
            ]),
        ],
        "routine": [
            ("Anytime (5 sec)", "Capture into the Inbox — phone or desktop."),
            ("Sunday (15 min)", "Weekly Review: clear the Inbox and check your projects."),
            ("Missed a week?", "Don't restart. Just do this week's review."),
        ],
        "tips": [
            "Never organise while capturing — that's the #1 reason second brains die.",
            "Search beats folders: press Ctrl/Cmd + K to find anything.",
            "Add a recurring Sunday reminder in your phone's calendar: \"Weekly Review — 15 min\".",
        ],
    },
    {
        "slug": "client-portal",
        "name": "Client Portal",
        "accent": "#d6a070",
        "tagline": "One link. Zero email chaos.",
        "intro": "A shareable Notion page for each client: what's next, what needs their review, files, feedback, meetings and invoices — so nobody digs through email again.",
        "inside": [
            ("Freelancer setup", "A 5-minute checklist at the top — delete it before sharing."),
            ("Project at a glance", "Project, timeline, your contact details and key links."),
            ("Coming up / Ready for review", "Next milestones and deliverables waiting for the client."),
            ("Milestones", "The project journey phase by phase, also as a timeline."),
            ("Deliverables", "Every file with its status."),
            ("Feedback & Blockers", "Client feedback in one place, plus a feedback form and a Waiting on You view."),
            ("Meeting Notes", "Every call summarised with decisions and next steps."),
            ("Invoices", "Amounts, due dates and payment status."),
            ("FAQ", "Client-facing answers on revisions, payments and contact."),
        ],
        "setup": [
            ("One portal per client", "Duplicate the portal page once for each client and rename it, e.g. \"Acme × Your Studio\"."),
            ("Fill in Project at a glance", "Project, dates, your contact and the 3 key links (contract, brief, shared folder)."),
            ("Replace the sample rows", "Add the real milestones, deliverables and invoices. Edit the FAQ: your email, revision rounds, payment terms."),
            ("Share with the client", "<b>Share → Invite</b> your client with <b>Can comment</b> (recommended). Need them to add rows? Give <b>Can edit content</b> or send them the <b>Send feedback</b> form. Then delete the setup block."),
        ],
        "sections": [
            ("Milestones & Deliverables", [
                "Milestones move Upcoming → In Progress → Done. Switch to Timeline to see them on a calendar.",
                "Set a deliverable to Ready for Review and it shows up at the top for your client.",
            ]),
            ("Feedback & Blockers", [
                "Clients leave feedback here (or via the form) instead of email.",
                "<b>Waiting on You</b> shows the client exactly what's blocking progress.",
            ]),
            ("Invoices", [
                "Status shows paid, pending or overdue — enter the paid date when money arrives.",
            ]),
            ("Before you share", [
                "Delete the setup block and the example rows; replace the sample email in the FAQ.",
                "Only invite the client — don't publish the page to the web unless you want it public.",
                "The Legal toggle at the bottom is for you; it tells clients they can ignore it.",
            ]),
        ],
        "routine": [
            ("Day one", "Send the client the portal link."),
            ("After every call", "Add a Meeting Notes row with decisions and next steps."),
            ("When you deliver", "Add the deliverable, set Ready for Review, tell the client in one line."),
            ("Weekly", "Update milestones, resolve feedback, check invoices."),
        ],
        "tips": [
            "Keep all feedback in the portal; politely redirect emailed feedback there.",
            "You may share your copies with your own clients — that's what it's for. Reselling the template is not allowed.",
        ],
    },
    {
        "slug": "student-os",
        "name": "Student OS",
        "accent": "#f6a064",
        "tagline": "Your whole school year, under control.",
        "intro": "Classes, assignments, exams, grades and GPA in one calm system — with study tracking that shows where your time really goes. For high school and college students anywhere in the world.",
        "inside": [
            ("This week", "Assignments due and upcoming exams, at the top of the page."),
            ("Courses", "One row per class — Grade %, Letter, GPA pts and On track fill in by themselves."),
            ("Assignments", "Everything due with a Days left countdown. Table, board and calendar views."),
            ("Exams", "Every test with a countdown and a spaced revision plan."),
            ("Study Sessions", "Each study block; time adds up per course and exam."),
            ("Grades", "Score, Max and Weight % — averages calculate themselves."),
            ("Class Schedule", "Your weekly timetable, grouped by day."),
            ("Notes & Habits", "Lecture notes with a review flag, and a daily habit score."),
        ],
        "setup": [
            ("Add your courses", "In <b>Courses</b>, add one row per class with term, credits (college) and a <b>Target %</b>."),
            ("Enter what's due", "Add every assignment and exam you know about, each linked to its course."),
            ("Fill your timetable", "Add your classes to <b>Class Schedule</b> by day and time."),
        ],
        "sections": [
            ("Grades & GPA (automatic)", [
                "Enter <b>Score</b>, <b>Max</b> and <b>Weight %</b> for each grade. The course's Grade %, Letter and GPA pts update instantly.",
                "<b>On track</b> compares your grade with your Target %.",
                "Your GPA: at the bottom of the <b>GPA pts</b> column, click → Calculate → Average.",
                "Uses the common US 4.0 scale. Different system? Edit the Letter and GPA pts formulas — Grade % works everywhere.",
            ]),
            ("Assignments & Exams", [
                "<b>Days left</b> counts down and turns 🔴 when something is overdue.",
                "Open an exam for a spaced revision plan (see Biology Midterm) — short sessions spread out beat one all-nighter.",
                "Click a Due date → turn on <b>Remind</b> to get a notification.",
            ]),
            ("Study Sessions", [
                "Log minutes and method per session. Courses and exams add up your time.",
                "The optional Time per course chart uses Notion's 1 free chart — skip it if you've used yours.",
            ]),
            ("New term", [
                "Set old courses to Completed and add new ones with the new term. The All terms view keeps your history.",
            ]),
        ],
        "routine": [
            ("Every morning (1 min)", "Check This week."),
            ("When you get work", "Add the assignment right away."),
            ("When a grade comes back", "Log it the same day."),
            ("Sunday (10 min)", "Plan the week's study blocks."),
        ],
        "tips": [
            "Test yourself instead of re-reading — active recall feels harder, that's why it works.",
            "Four 30-minute sessions over two weeks beat one 2-hour cram.",
            "Add Student OS to Favourites in the Notion app — This week is right at the top.",
        ],
        "faq": [
            ("Which Notion plan do I need?", "The free plan. Everything works free."),
            ("High school or college?", "Both. Use Credits for college, ignore them in high school."),
            ("My school uses a different grading system.", "Edit the Letter and GPA pts formulas in Courses. Grade % works for every system."),
            ("Something isn't working?", "Email info@templyworks.com with a screenshot."),
        ],
        "licence": "Licence: for your own studies and personal life. Reselling, sharing or publishing the template is not allowed. Digital product — all sales are final once delivered. Statutory rights for defective content remain unaffected. Not academic advice — always follow your school's official grading rules. (You agreed to immediate delivery at checkout.)",
    },
    {
        "slug": "custom-template",
        "kind": "service",
        "name": "Custom Template",
        "tagline": "Your personal Notion system — built for you.",
        "cover_label": "YOUR CUSTOM BUILD GUIDE",
        "ver": "Custom build guide · Version Oct 2026",
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
]

COMMON_START_DE = [
    ("Template duplizieren", "Öffne den Link aus deiner Bestell-E-Mail. Klicke oben rechts auf ··· und dann auf <b>Duplizieren</b>. Arbeite nur in deiner Kopie."),
    ("Beispiele löschen", "Jede Datenbank enthält ein paar Beispielzeilen. Schau sie dir an und lösche sie dann (Zeilen markieren → Löschen) oder überschreibe sie mit deinen Daten."),
    ("Als Favorit markieren", "Klicke oben auf den Stern (☆). So findest du das System in der Seitenleiste und am Handy unter Favoriten."),
]
