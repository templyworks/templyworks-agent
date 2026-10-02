# Templyworks Dev Toolkit

Technical companion to the business agents — **code-level Shopify work**: theme edits, Liquid sections, GraphQL, store automation. The 9 business agents handle strategy and content; this handles implementation.

## Store Configuration (verified 2026-09-30)

```yaml
shop_name: Templyworks
myshopify_domain: h2ymub-td.myshopify.com
live_domain: templyworks.com
currency: USD   # Shopify Markets shows local currency at checkout
tax_status: Kleinunternehmerregelung §19 UStG — all variants taxable:false, no VAT charged
owner_email: info@templyworks.com

theme_live: "Templyworks v3.11"
theme_live_id: gid://shopify/OnlineStoreTheme/209826021725   # MAIN since 2026-09-30 — API writes BLOCKED
theme_draft: "Copy of Templyworks v3.11"   # id 210510086493 — has withdrawal-consent snippet (snippets/tw-withdrawal-consent.liquid, rendered from snippets/meta-tags.liquid); Kevin must publish
theme_unused: "Clarity"
theme_unused_id: gid://shopify/OnlineStoreTheme/208718365021
```

⚠️ **Rule:** Theme writes via API only work on **unpublished** themes. For the live theme, give Kevin paste-ready code for Online Store → Themes → Edit code. Never publish a theme — Kevin clicks Publish himself.

"Templyworks trial", "Tinker" and "Templyworks v3.2" no longer exist. Ignore old references to them.

## Product Catalog

| Product | Price | Taxable | Type |
|---|---|---|---|
| Finance HQ | $19 | false | Notion template |
| Client Pipeline | $19 | false | Notion template |
| Project Tracker | $19 | false | Notion template |
| Pitch Kit | $19 | false | Notion template |
| Second Brain | $19 | false | Notion template |
| Client Portal | $19 | false | Notion template |
| Abitur System | $19 | false | Notion template (German) |
| Client Machine | $44 (compare $57) | false | Bundle: Client Pipeline + Pitch Kit + Client Portal |
| Solo Ops | $44 (compare $57) | false | Bundle: Finance HQ + Project Tracker + Second Brain |
| Custom Template Request | $149 | false | Service |

GIDs in `shopify-graphql.md`.

## Folder Structure

```
/dev-toolkit
  README.md              — this file, store config
  shopify-graphql.md     — queries/mutations for this store
  theme-editing.md       — theme structure, sections, safe edit workflow
  brand-system.md        — design tokens (green palette, light/dark)
  automation-scripts.md  — reusable workflows (launch, delivery, tax checks)
```

## Quick Reference: Brand Tokens (dark mode)

```css
--tw-bg: #061210;
--tw-green: #2f8f5b;
--tw-green-hover: #1c5c3a;
--tw-green-bright: #4fbe80;
--tw-green-light: #6fd699;
--tw-text-muted: rgba(255,255,255,0.46);
--tw-border: rgba(255,255,255,0.075);
--tw-border-accent: rgba(47,143,91,0.3);
--font: -apple-system, 'Inter', BlinkMacSystemFont, sans-serif;
```
Light mode tokens in `brand-system.md`.

## How This Connects to the Business Agents

The **Ops agent** is the bridge. Example:
```
Revenue agent → "Build a new bundle at $69"
  → Ops agent reads shopify-graphql.md
  → Creates product, sets taxable:false
  → Adds section/card changes on a DRAFT copy of the live theme
  → Kevin previews + publishes
```
