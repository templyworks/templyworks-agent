# Theme Editing Guide — TemplyWorks

## The One Rule

**Templyworks trial** (`205023969629`) is the live/active theme. Every edit goes here. Tinker (`205135151453`) is a placeholder — confirmed by Kevin, never touch it again.

## Current Custom Sections (already built, live on Templyworks trial)

| File | Purpose |
|---|---|
| `sections/templyworks-3d-hero.liquid` | Homepage hero — Three.js 3D orbiting cards, headline, product grid, CTA strip |
| `assets/tw-header.css` | Header override — branded logo, purple CTA, single-row nav |
| `assets/tw-test.css` | Leftover test file from write-access verification — safe to delete |

## Section File Anatomy (for any new section)

```liquid
{% comment %} Description {% endcomment %}
<style>
  /* scope everything to a unique ID to avoid theme CSS collisions */
  #tw-[section-name] { ... }
</style>

<div id="tw-[section-name]">
  ...content...
</div>

<script>
  /* any JS, scoped/IIFE wrapped */
</script>

{% schema %}
{
  "name": "Section Name",
  "settings": [],
  "presets": [{"name": "Section Name"}]
}
{% endschema %}
```

## Wiring a Section to a Template

`templates/index.json` (homepage) controls section order:
```json
{
  "sections": {
    "templyworks_hero": { "type": "templyworks-3d-hero", "settings": {} }
  },
  "order": ["templyworks_hero"]
}
```

## Safe Edit Workflow

1. Read the existing file first (never blind-overwrite)
2. Make the change
3. Upload via `themeFilesUpsert`
4. Preview at `templyworks.com/?preview_theme_id=205023969629`
5. Screenshot/verify before calling it done
6. Never publish a theme programmatically — that's Kevin's manual click (Online Store → Themes → Publish)

## Known Issues Already Fixed

- ✅ "Powered by Shopify" footer branding — hidden via CSS in `base.css`
- ✅ Header logo — branded "TemplyWorks" wordmark with purple "Works"
- ✅ Header CTA — "Get templates →" button added
- ✅ Nav wrapping to 2 rows — fixed via CSS grid + reduced padding
- ✅ Duplicate nav/logo when 3D hero was first added — removed nav from section, let theme header handle it

## Brand Visual Language (for consistency in new sections)

- Background: near-black `#080810`, never pure black
- Accent: purple `#7c3aed`, hover `#6d28d9`
- Text: white headlines, `rgba(255,255,255,0.5)` for muted/secondary
- Borders: `rgba(124,58,237,0.18)` for purple-tinted dividers, `rgba(255,255,255,0.08)` for neutral
- Typography: Inter / -apple-system, weight 700-900 for headlines, 400-500 for body
- Buttons: solid purple primary, ghost/outline secondary
- Cards: `rgba(255,255,255,0.03)` background, `rgba(255,255,255,0.08)` border, 16px radius
- Always mobile-responsive — test at 768px breakpoint minimum
