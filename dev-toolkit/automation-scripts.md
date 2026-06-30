# Automation Scripts & Patterns — TemplyWorks

Reusable workflows for common technical tasks. Reference these instead of rebuilding from scratch each time.

## 1. New Product Launch (full sequence)

```
1. Create product (productCreate mutation)
   - Set taxable: false on all variants (Kleinunternehmer compliance)
   - Set price in EUR
2. Write SEO product description (Growth agent → growth-agent.md template)
3. Generate product image / mockup
4. Add to relevant collections
5. Configure EDP digital delivery link (Notion share URL)
6. Add to homepage product grid (templyworks-3d-hero.liquid → tw-grid section)
7. Write launch content (Marketing agent → 8-day launch sequence)
8. Verify in Templyworks trial preview before going live
```

## 2. EDP Digital Delivery Setup

EDP (Easy Digital Products) free plan = max 3 products. For 6+ products, either:
- Upgrade EDP plan, or
- Use Shopify's native order confirmation email + manual Notion link in product metafield as fallback

Setup per product:
1. Shopify Admin → Apps → EDP → Digital Products → Create digital product
2. Link to the corresponding Shopify product
3. Add the Notion template share URL (format: `notion.so/[workspace]/[page-id]?pvs=4`)
4. Set delivery trigger: "Order paid"
5. Test with a $0 test order before going live

## 3. Tax Compliance Check (run periodically)

```graphql
{
  products(first: 20) {
    edges {
      node {
        title
        variants(first: 3) {
          edges { node { taxable } }
        }
      }
    }
  }
}
```
Any `taxable: true` found → flag immediately, fix via `productVariantsBulkUpdate`. See `shopify-graphql.md` for the exact mutation.

## 4. Revenue Threshold Monitoring

```graphql
{
  orders(first: 250, query: "created_at:>[year-start]") {
    edges {
      node { totalPriceSet { shopMoney { amount } } }
    }
  }
}
```
Sum all amounts. Alert at €18,000 (consult Steuerberater), hard stop at €22,000 (Kleinunternehmer threshold — must switch tax model).

## 5. Theme Section Deploy Checklist

```
[ ] Read current file state before editing (never blind overwrite)
[ ] Confirm target theme is Templyworks trial (205023969629), NOT Tinker
[ ] Upload via themeFilesUpsert
[ ] Preview at templyworks.com/?preview_theme_id=205023969629
[ ] Check mobile breakpoint (768px)
[ ] Screenshot to verify visually
[ ] Report back — never assume success without checking
```

## 6. Weekly Store Health Check

```
1. Check all 8 products: Active status, correct pricing, taxable: false
2. Check legal pages: all 8 published (Impressum, Privacy, Terms, Refund, About, FAQ, Contact, Custom Request)
3. Check orders: any pending delivery issues
4. Check theme: Templyworks trial still the live/active theme
5. Check revenue: running total vs €22,000 threshold
```

## 7. Common GraphQL Gotchas (learned from real sessions)

- `themeFilesUpsert` on the **live published theme** may be blocked by safety policy in some environments — fallback to manual theme code editor if so
- Fuzzy title queries (`title:Something*`) can silently match the wrong product — always cross-check against a full product list with exact GIDs
- HTML entities (`&euro;`, `&mdash;`) required in Liquid file uploads — raw unicode can cause encoding issues
- Variant IDs and Product IDs are different GIDs — mutations often need both, don't mix them up
