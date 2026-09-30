# Theme Editing Guide — Templyworks

## The Rules

1. **Live theme = Templyworks v3.1** (`209826021725`, published 2026-09-30). API writes are blocked. Changes go through Kevin: give paste-ready code + exact file + exact location.
2. **Draft theme = none right now** (v3.2 was deleted). For API work, Kevin duplicates v3.1 → Claude edits the copy → Kevin publishes.
3. Never publish a theme programmatically.
4. Live and draft can drift. Before publishing a draft, compare file checksums so nothing edited on live is lost.

## Theme Structure (Dawn-based, heavily customized)

### Layout
- `layout/theme.liquid` — renders `snippets/tw-theme-mode` in `<head>` (light/dark toggle, FOUC guard), `header-group`, `main`, `footer-group`

### Header group (`sections/header-group.json`, in order)
| Section | Purpose |
|---|---|
| `tw-premium` | JSON-LD (Organization, WebSite, Breadcrumbs), scroll progress bar, ambient orbs, grain, reveal-on-scroll for Dawn sections |
| `tw-topbar` | Rotating announcement bar |
| `header` | Dawn header (logo "Templyworks", nav) |
| `tw-lightmode` | Light-mode overrides for tw-home, tw-about, tw-contact, tw-custom-request, topbar |
| `tw-lightmode-pages` | Light mode for `.tw-page` bodies, PERF guard, drawer fix, **scroll fix** |
| `tw-mobile-menu` | Branded mobile drawer + scrim + CTA |

### Footer group (`sections/footer-group.json`)
| Section | Purpose |
|---|---|
| `templyworks-footer` | Custom footer, §19 notice |
| `tw-motion` | Logo casing fix, alt-text fix, reveal failsafe, motion |

### Page sections / templates
| Template | Section | Page |
|---|---|---|
| `index.json` | `tw-home` / `templyworks-3d-hero` | Homepage |
| `page.about-v2.json`, `page.about.json` | `tw-about` (#twab) | About |
| `page.custom-v2.json` | `tw-custom-request` (#twcr) | Custom Template Request |
| `page.contact.json` | `tw-contact` (#twct) | Contact |
| `page.json` | `main-page` | FAQ, Imprint, legal pages (`.tw-page` HTML in page body) |
| `product.json` | `main-product` | Products |

### Assets
- `tw-button-unify.css` — loaded in theme.liquid
- `tw-header.css` — **not loaded** in the layout (legacy); don't rely on it
- `tw-test.css`, `tw-logo-test.png` — leftovers, safe to delete

## Section File Anatomy

```liquid
{% comment %} Description {% endcomment %}
<style>
  /* scope everything to a unique ID */
  #tw-[name] { ... }
  /* + light mode */
  html[data-theme='light'] #tw-[name] { ... }
</style>

<div id="tw-[name]">
  ...content...
</div>

<script>
  (function(){ /* scoped JS */ })();
</script>

{% schema %}
{ "name": "Section Name", "settings": [], "presets": [{"name": "Section Name"}] }
{% endschema %}
```

Use Liquid for prices (`{{ product.price | money_with_currency }}`) — never hardcode $ or €.

## Safe Edit Workflow

1. Read the existing file from the target theme first
2. Edit (keep full file — upsert replaces the whole file)
3. Upload via `themeFilesUpsert` to the **draft copy**
4. Preview: `https://templyworks.com/[path]?preview_theme_id=[draft id]`
5. Verify mobile (≤768px) + desktop, light + dark, scrolling
6. Tell Kevin what changed; he publishes

## Known Issues / Fix Log

- ✅ "Powered by Shopify" hidden (base.css)
- ✅ Logo casing "Templyworks" (tw-motion)
- ✅ Mobile drawer scrim/chevron (tw-mobile-menu, tw-lightmode-pages)
- ✅ Blank-page reveal bug — failsafe in tw-motion
- ✅ About + Custom Template pages not scrolling — fixed in `tw-lightmode-pages` (force html/body scroll, `overflow-x:clip` on #twab/#twcr, no blur orbs, no fixed background). Live since v3.1 publish 2026-09-30.

## Brand Visual Language

See `brand-system.md`. Short version: bg `#061210`, green `#2f8f5b` buttons, `#4fbe80` accents, white headlines, 16px card radius, always light-mode rules, no heavy blur.
