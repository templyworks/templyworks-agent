# Shopify GraphQL Reference — TemplyWorks

Tested, working mutations/queries for this specific store. Copy-paste ready.

## ⚠️ Before Any Theme Write

```
ALWAYS target theme: gid://shopify/OnlineStoreTheme/205023969629 ("Templyworks trial")
NEVER target: gid://shopify/OnlineStoreTheme/205135151453 ("Tinker" — placeholder only)
```

Live/main theme writes may be blocked by safety policy depending on environment — if so, edit via the Shopify theme code editor UI directly (Online Store → Themes → Templyworks trial → Edit code) instead of the API.

## Get Theme IDs

```graphql
{
  themes(first: 10) {
    nodes { id name role }
  }
}
```

## Upload/Update a Theme File

```graphql
mutation ThemeFilesUpsert($themeId: ID!, $files: [OnlineStoreThemeFilesUpsertFileInput!]!) {
  themeFilesUpsert(themeId: $themeId, files: $files) {
    upsertedThemeFiles { filename }
    userErrors { field message }
  }
}
```
Variables:
```json
{
  "themeId": "gid://shopify/OnlineStoreTheme/205023969629",
  "files": [
    {
      "filename": "sections/my-section.liquid",
      "body": { "type": "TEXT", "value": "...liquid code..." }
    }
  ]
}
```

## Read a Theme File

```graphql
{
  theme(id: "gid://shopify/OnlineStoreTheme/205023969629") {
    files(filenames: ["sections/header.liquid"], first: 1) {
      nodes {
        filename
        body { ... on OnlineStoreThemeFileBodyText { content } }
      }
    }
  }
}
```

## List All Products

```graphql
{
  products(first: 20) {
    edges {
      node {
        id
        title
        variants(first: 3) {
          edges { node { id taxable price } }
        }
      }
    }
  }
}
```

## Fix Product Tax Status (Kleinunternehmer compliance)

```graphql
mutation UpdateVariantTax($input: ProductVariantsBulkInput!, $productId: ID!) {
  productVariantsBulkUpdate(productId: $productId, variants: [$input]) {
    productVariants { id taxable }
    userErrors { field message }
  }
}
```
Variables: `{ "input": { "id": "[variant gid]", "taxable": false }, "productId": "[product gid]" }`

## Check Orders / Revenue (for §19 UStG threshold tracking)

```graphql
{
  orders(first": 50, query: "created_at:>2026-01-01") {
    edges {
      node {
        id
        createdAt
        totalPriceSet { shopMoney { amount currencyCode } }
        taxLines { rate }
      }
    }
  }
}
```
`taxLines` should always be `[]` — confirms no VAT charged.

## Get Legal Pages Content

```graphql
{
  pages(first: 20) {
    edges {
      node { handle title isPublished bodySummary }
    }
  }
}
```

## Read Specific Page Body

```graphql
{
  pages(first: 1, query: "handle:imprint") {
    edges { node { body } }
  }
}
```

## Product Catalog Reference (current as of last audit)

| Handle pattern | Product | GID |
|---|---|---|
| finance-hq-* | Finance HQ | 16245061583197 |
| second-brain-* | Second Brain | 16246052323677 |
| client-pipeline-* | Client Pipeline | 16246055371101 |
| project-tracker-* | Project Tracker | 16246056354141 |
| client-portal-* | Client Portal | 16246058058077 |
| pitch-kit-* | Pitch Kit | 16246061105501 |
| custom-template-request | Custom Template Request | 16272542630237 |
| freelancer-os-* | Freelancer OS bundle | 16276250034525 |

Prefix all with `gid://shopify/Product/[number]`

## Common Mistakes (learned the hard way)

1. **Title-based product queries can mismatch.** `query: "title:Freelancer*"` once matched a wrong product. Always verify by listing all products first and reading exact titles, not assuming a fuzzy match is correct.
2. **Don't touch Tinker.** It's the placeholder/backup. All real work is on Templyworks trial.
3. **Theme preview URL format:** `https://templyworks.com/?preview_theme_id=205023969629`
4. **HTML entities required in Liquid `{% schema %}` JSON strings and in raw HTML** — use `&euro;`, `&mdash;`, `&rarr;` etc. instead of raw unicode to avoid encoding issues in theme file uploads.
