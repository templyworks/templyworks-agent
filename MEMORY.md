# Templyworks — Permanent Memory

Read this first. These rules override anything else in this repo or in chat history.

## Rules from Kevin (permanent)
- **Name: "Templyworks"** — capital T, lowercase w, one word. Never "TemplyWorks". All copy, emails, product pages, code comments, outputs.
- Never publish a theme or send customer emails without Kevin's OK.
- Always verify live state in Shopify before stating theme, prices or products — docs drift.

## Live store facts (re-verified in Shopify 2026-10-16)
- Live theme: **Templyworks v3.13** — `gid://shopify/OnlineStoreTheme/210980831581` (MAIN since 2026-10-17, API writes blocked; v3.12 kept as backup)
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
- Pitch Kit Services board: Good → Better → Best (fixed in UI 2026-10-17), "No Tier" hidden.
- Guides rebuilt 2026-10-17 (guides/*.pdf, Student OS added, Abitur removed). Copies on Kevin's Mac: Downloads/Templyworks-Guides. Uploading to Digital Products needs Kevin (file picker); then delete old PDFs in app UI.

## 2026-10-17 — Full audit (Customer/Ops/Legal/Growth/Intel agents)
- WARNING: Shopify MCP `upload-digital-product-file` REPLACES all assets (Notion links get wiped). After any upload, re-add links in Digital Products app (Add asset → Link; when asked "Send customers the updated file?" choose Don't send update).
- Fixed: links restored on 8 products; bundle "price of two" claim; refund FAQ wording (statutory rights); Finance HQ plan FAQ; Client Portal guest-limit note; Student OS taxable=false + frontpage; legacy SKU TW-ABITUR-LEGACY; Custom Template rebuilt description + SEO title; focus-row H3 labels in 5 templates; Saffron tasks (progress 50%); invoices total 8,500; example.com emails; Lumen deal 2,500; Habits/Invoices sorted; Pitch Kit views renamed (Open proposals).
- Open (needs Kevin): homepage shows Clarity "We'll be back soon" (maintenance); Finance HQ PDF upload; Legal policy updates (Custom service withdrawal exception, statutory-rights line in Refund Policy, privacy §5 processors, seller name in Terms §1, one Terms page); test purchase; Notion UI: Progress % decimals, Scoreboard group order.
- Analytics 90d: 316 sessions, 1 order, 0.32% CVR; no TikTok pixel; competitors show live preview + demo video + reviews.

- 2026-10-17: Add-to-cart button was button--secondary (dynamic checkout on) → near invisible in dark/light. Fixed with solid-green override in assets/tw-button-unify.css on Templyworks v3.12 (unpublished; writes work while unpublished).

## 2026-10-17 — Legal update
- Pages updated live (refund-policy, terms-of-service, privacy-policy, imprint, faq, right-of-withdrawal): seller identity, §3a Custom service withdrawal (§356(4)/§357a BGB), statutory-rights line, processors (Shopify Digital Products, Consentmo, Notion, Google Workspace), reply time 1–2 business days.
- Shopify *policies* (/policies/*) need write_legal_policies scope — NOT available via API. Kevin pastes legal-drafts/*.html via Settings → Policies → <> HTML.
- Theme "Templyworks v3.13" (gid://shopify/OnlineStoreTheme/210980831581): combined checkout consent (digital + custom service). Needs Kevin to publish.
