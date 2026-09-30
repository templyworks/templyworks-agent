# Shopify GraphQL Reference — Templyworks

Tested queries/mutations for this store.

## ⚠️ Before Any Theme Write

```
LIVE (blocked):  gid://shopify/OnlineStoreTheme/209826021725  ("Templyworks v3.1", MAIN since 2026-09-30)
DRAFT:           none right now — Kevin must duplicate v3.1 in admin to create one
```
`themeFilesUpsert` on the MAIN theme is refused by the connector's safety policy. Edit a draft copy, or give Kevin code for the Shopify code editor.

Always run the themes query first — IDs change whenever Kevin duplicates/publishes.

## Get Theme IDs

```graphql
{ themes(first: 10) { nodes { id name role } } }
```

## List Theme Files (supports wildcards)

```graphql
{
  theme(id: "[THEME_GID]") {
    files(filenames: ["sections/*", "templates/*"], first: 250) {
      nodes { filename size }
    }
  }
}
```

## Read a Theme File

```graphql
{
  theme(id: "[THEME_GID]") {
    files(filenames: ["sections/tw-about.liquid"], first: 1) {
      nodes {
        filename
        checksumMd5
        body { ... on OnlineStoreThemeFileBodyText { content } }
      }
    }
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
  "themeId": "[DRAFT_THEME_GID]",
  "files": [
    { "filename": "sections/my-section.liquid",
      "body": { "type": "TEXT", "value": "...full file content..." } }
  ]
}
```

## List Products (with price + tax)

```graphql
{
  products(first: 30) {
    nodes {
      id title handle status
      variants(first: 3) { nodes { id price compareAtPrice taxable } }
    }
  }
}
```
Note: `requiresShipping` does not exist on `ProductVariant` in the current API version.

## Fix Product Tax Status

```graphql
mutation UpdateVariantTax($productId: ID!, $variants: [ProductVariantsBulkInput!]!) {
  productVariantsBulkUpdate(productId: $productId, variants: $variants) {
    productVariants { id taxable }
    userErrors { field message }
  }
}
```
Variables: `{ "productId": "[product gid]", "variants": [{ "id": "[variant gid]", "taxable": false }] }`

## Orders / Revenue (threshold tracking)

```graphql
{
  orders(first: 50, query: "created_at:>=2026-01-01") {
    nodes {
      id createdAt
      totalPriceSet { shopMoney { amount currencyCode } }
      taxLines { rate }
      billingAddress { countryCodeV2 }
    }
    pageInfo { hasNextPage endCursor }
  }
}
```
`taxLines` should be `[]`. Amounts are USD — convert to EUR for §19. Country code needed for EU OSS tracking.

## Pages

```graphql
{ pages(first: 30) { nodes { handle title templateSuffix isPublished } } }
```
Skip `body` in list queries — some pages (GDPR/Consentmo) are huge and truncate output.

## Shop Info

```graphql
{ shop { name currencyCode myshopifyDomain primaryDomain { host } } }
```

## Product Catalog Reference (2026-09-30)

| Product | Handle | GID |
|---|---|---|
| Finance HQ | finance-hq-notion-personal-finance-dashboard | 16245061583197 |
| Second Brain | second-brain-notion-para-knowledge-system | 16246052323677 |
| Client Pipeline | client-pipeline-notion-crm-for-freelancers | 16246055371101 |
| Project Tracker | project-tracker-notion-project-task-manager | 16246056354141 |
| Client Portal | client-portal-notion-workspace-for-freelancers-clients | 16246058058077 |
| Pitch Kit | pitch-kit-notion-proposals-services-library | 16246061105501 |
| Custom Template Request | custom-template-request-your-personal-notion-system | 16272542630237 |
| Abitur System | abitur-system-notion-command-center-for-the-german-oberstufe | 16456472691037 |
| Client Machine (bundle) | client-machine-notion-bundle | 16467109019997 |
| Solo Ops (bundle) | solo-ops-notion-bundle | 16467110953309 |

Prefix: `gid://shopify/Product/[number]`. The old "Freelancer OS" bundle no longer exists.

## Common Mistakes

1. **Fuzzy title queries mismatch.** List all products and match exact GIDs.
2. **Writing to the live theme** — blocked. Use a duplicated draft.
3. **Hardcoding currency** — store is USD with local display; use Liquid money filters.
4. **HTML entities in Liquid** — use `&mdash;`, `&rarr;` etc. instead of raw unicode in theme uploads.
5. **Partial upserts** — `themeFilesUpsert` replaces the whole file; always send full content.
