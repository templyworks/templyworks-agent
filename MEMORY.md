# Templyworks — Permanent Memory

Read this first. These rules override anything else in this repo or in chat history.

## Rules from Kevin (permanent)
- **Name: "Templyworks"** — capital T, lowercase w, one word. Never "TemplyWorks". All copy, emails, product pages, code comments, outputs.
- Never publish a theme or send customer emails without Kevin's OK.
- Always verify live state in Shopify before stating theme, prices or products — docs drift.

## Live store facts (re-verified in Shopify 2026-10-16)
- Live theme: **Templyworks v3.12** — `gid://shopify/OnlineStoreTheme/210510086493` (MAIN, API writes blocked)
- Gone: "Templyworks trial", "Tinker", v3.1, v3.11, v3.2
- Logo: no image. Text wordmark "Temply" white + "works" green `#2f8f5b`, weight 800 (`sections/header.liquid`)
- Brand colors: green, NOT purple. bg `#071310` (scheme-1) / `#061210` (custom sections), accent `#2f8f5b`, hover `#1c5c3a`, bright `#4fbe80`
- Favicon: `templyworks-favicon-tw-green.png`
- Socials: instagram.com/templyworks_ · tiktok.com/@templyworks

Details: `dev-toolkit/README.md`, `dev-toolkit/brand-system.md`.

## Store snapshot (2026-10-16)
- 10 active products, all `taxable:false`, prices match README ($19 templates · $44 bundles · $149 Custom)
- Orders: 2 total — #1001 (test, €0, 2026-05-14), #1006 ($19.40, 2026-07-29). No sales since.

## Social log
- 2026-10-15 TikTok video: 777 views

## 2026-10-16 — Template overhaul
- Research: research/template-buyer-research-2026-10.md (why buyers quit; 6 design rules).
- All 6 masters + new Student OS got: green header, "Your routine" callout, focus row (linked views), helper text per section, Tips/FAQ/License toggles.
- Sample data fixed: relations were empty (Client Pipeline, Project Tracker, Pitch Kit) → linked; stale June dates → Aug–Oct 2026; Finance HQ now has 3 months of transactions; internal Templyworks text removed from Second Brain.
- Boards: empty "No ..." groups hidden, stage order fixed (Pitch Kit, Project Tracker tasks, Class Schedule days).
- Delivery app = Shopify Digital Products (docs said EDP — fixed).
- Pending: Kevin publishes Student OS → swap Shopify product 16642871951709; new descriptions, PDFs, images/covers; store test.

## 2026-10-16 — Product overhaul
- Student OS = Shopify product 16642871951709 (handle student-os-notion-student-planner, delivers https://cute-herring-2b2.notion.site/Student-OS-3fb6bb63c14f81fca1dffb5272690f0d). Old Abitur product 16456472691037 ARCHIVED (Digital Products link could not be edited via API). Old Abitur URL 301 → Student OS. Abitur Notion master in Trash.
- All 7 products: Amazon-style descriptions (product-images/descriptions.py), new 4-image sets (product-images/out/*-v2/v3.png), SEO titles/descriptions.
- Bundles: new v2 hero + inside images (make_bundle_images.py) + Amazon-style descriptions; then the 3 single heroes.
- Finance HQ Budgets: "Spent" is now a rounded formula over hidden rollup "Spent (sum)".
- Pitch Kit Services board view renamed "Best / Better / Good" (API cannot reorder manual groups; "No Tier" hidden).
- Quick-Start PDFs in Digital Products are older versions; replacing needs upload in Shopify admin (file picker).
