# TemplyWorks Dev Toolkit

Technical companion to `/agents` — this folder is for **code-level Shopify work**: theme edits, Liquid sections, GraphQL mutations, store automation scripts. The 9 business agents in `/agents` handle strategy and content; this handles implementation.

## Store Configuration (memorize this before any task)

```yaml
store_handle: templyworks
domain: h2ymub-td.myshopify.com
live_domain: templyworks.com
theme_live: "Templyworks trial"
theme_live_id: gid://shopify/OnlineStoreTheme/205023969629
theme_placeholder: "Tinker"
theme_placeholder_id: gid://shopify/OnlineStoreTheme/205135151453
currency: EUR
tax_status: Kleinunternehmerregelung §19 UStG — all products taxable:false, no VAT charged
owner_email: info@templyworks.com
```

⚠️ **Critical rule:** ALL theme edits go to **Templyworks trial** (`205023969629`). NEVER touch Tinker — it's a placeholder/backup theme only. Confirmed by Kevin — do not forget this again.

## Product Catalog Reference

| Product | Price | Taxable | Type |
|---|---|---|---|
| Finance HQ | €9.99 | false | Notion Template |
| Client Pipeline | €9.99 | false | Notion Template |
| Project Tracker | €9.99 | false | Notion Template |
| Pitch Kit | €9.99 | false | Notion Template |
| Second Brain | €9.99 | false | Notion Template |
| Client Portal | €9.99 | false | Notion Template |
| Custom Template Request | €49.99 | false | Custom Service |
| Freelancer OS (bundle) | €34.99 | false | Notion Bundle |

## Folder Structure

```
/dev-toolkit
  README.md              — this file, store config
  shopify-graphql.md      — common mutations/queries used for this store
  theme-editing.md        — Liquid section patterns, how to safely edit Templyworks trial
  brand-system.md         — design tokens (colors, fonts) for any new sections
  automation-scripts.md   — reusable patterns (EDP setup, tax fixes, etc.)
```

## Quick Reference: Brand Tokens

```css
--tw-bg: #080810;
--tw-purple: #7c3aed;
--tw-purple-hover: #6d28d9;
--tw-purple-light: #a78bfa;
--tw-purple-lighter: #c4b5fd;
--tw-text-muted: rgba(255,255,255,0.5);
--tw-border: rgba(255,255,255,0.08);
--tw-border-accent: rgba(124,58,237,0.18);
--font: -apple-system, 'Inter', BlinkMacSystemFont, sans-serif;
```

## How to Use This With the 9 Business Agents

The **Ops agent** (in `/agents/ops-agent.md`) is the bridge — when a business agent identifies a technical need (e.g. Revenue agent wants a new bundle, Marketing agent wants a landing page), Ops agent executes it using the patterns in this toolkit.

Example flow:
```
Revenue agent → "Build a Q3 bundle at €19.99"
  → Ops agent reads /dev-toolkit/shopify-graphql.md
  → Creates product via productCreate mutation
  → Sets taxable: false (per tax_status above)
  → Confirms in Templyworks trial theme only
```
