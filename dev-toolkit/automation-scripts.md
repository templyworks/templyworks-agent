# Automation Scripts & Patterns — Templyworks

Reusable workflows. Use these instead of rebuilding from scratch.

## 1. New Product Launch

```
1. Build/finish the master template in Notion (Ops) — note the page ID
2. Create product (productCreate)
   - Price in USD ($19 standard template)
   - taxable: false on all variants
   - Title format: "[Name] — Notion [Category] for [Audience]"
3. SEO description (Growth agent)
4. Product images / mockups
5. Add to collections (all-templates + relevant ones)
6. Configure delivery (EDP) with the Notion duplicate link
7. Decide bundle fit (Revenue) — update bundle products if needed
8. Theme: add product card/section on DRAFT theme (v3.1), preview
9. Launch content (Marketing → 8-day launch)
10. Kevin publishes theme + announces
```

## 2. Digital Delivery Setup (EDP)

EDP free plan = limited products. With 10 products (incl. 2 bundles), confirm the plan covers all of them.

Per product:
1. Shopify Admin → Apps → EDP → Digital Products → Create
2. Link the Shopify product
3. Add Notion duplicate/share URL
4. Bundles: add all 3 template links
5. Trigger: "Order paid"
6. Test with a 100%-off test discount order

## 3. Tax Compliance Check

```graphql
{ products(first: 30) { nodes { title variants(first: 3) { nodes { taxable } } } } }
```
Any `taxable: true` → fix with `productVariantsBulkUpdate` (see `shopify-graphql.md`).

## 4. Revenue Threshold Monitoring

Pull paid orders for the year (paginate), sum `totalPriceSet.shopMoney.amount` (USD), convert to EUR.
- §19 UStG (since 2025): prior year ≤ €25,000, current year ≤ €100,000 — crossing €100k ends the exemption immediately
- EU cross-border B2C digital sales: > €10,000/year → OSS / destination VAT
- Alert Kevin around €20,000/year to plan with a Steuerberater

## 5. Theme Change Deploy Checklist

```
[ ] Run themes query — confirm current IDs
[ ] Read current file from the DRAFT theme (v3.1, 209826021725)
[ ] Upsert full file to the draft
[ ] Preview: templyworks.com/[path]?preview_theme_id=209826021725
[ ] Check mobile (≤768px), desktop, light + dark mode, scrolling
[ ] If the live theme needs the same change: give Kevin paste-ready code + file + spot
[ ] Report back — never assume success without checking
```

## 6. Weekly Store Health Check

```
1. All 10 products ACTIVE, correct price, taxable:false
2. Pages: Imprint, Terms, Refund, Right of Withdrawal, FAQ, About, Contact, Custom Request published
   (privacy-policy PAGE is unpublished — Shopify policy used instead; confirm policy exists)
3. Orders: any delivery issues
4. Theme: which theme is MAIN (IDs change on duplicate/publish)
5. Revenue: running total vs thresholds (item 4)
```

## 7. Notion Template Edits

```
1. Find master page (IDs in ops-agent.md) via Notion connector
2. Tell Kevin what will change — edits hit all NEW buyers
3. Make the change
4. If it's a meaningful update: note it for a "free lifetime update" email to past buyers
```

## 8. GraphQL Gotchas

- Live theme writes blocked — draft only
- Fuzzy title queries can hit the wrong product — use GIDs
- Use HTML entities in Liquid uploads
- Variant IDs ≠ Product IDs
- Big page bodies (GDPR page) truncate tool output — don't request `body` in list queries
