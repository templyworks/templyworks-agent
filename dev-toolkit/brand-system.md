# Brand System — Templyworks

## Identity

**Name:** Templyworks — capital T, lowercase w. (Old "TemplyWorks" spelling retired; the theme rewrites the logo text to "Templyworks".)
**Tagline direction:** "We turn chaos into systems." / "Stop building from scratch."
**Positioning:** A Notion design studio from Hamburg.
**Voice:** Direct, confident, calm. Not corporate, not hype-y. Real benefits over productivity-guru language.

## Colors — Dark mode (default)

```css
--tw-bg: #061210;              /* page background (deep green-black) */
--tw-panel: #0b1a16;           /* cards / panels */
--tw-green: #2f8f5b;           /* primary accent, buttons */
--tw-green-hover: #1c5c3a;     /* button hover */
--tw-green-bright: #4fbe80;    /* eyebrows, tags, links */
--tw-green-light: #6fd699;     /* gradient end, hover links */
--tw-green-deep: #14432a;      /* darkest accent */
--tw-text-primary: #ffffff;
--tw-text-muted: rgba(255,255,255,0.46);
--tw-text-faint: rgba(255,255,255,0.32);
--tw-border: rgba(255,255,255,0.075);
--tw-border-accent: rgba(47,143,91,0.3);
```

## Colors — Light mode (toggle in header, stored in localStorage `tw-theme`)

```css
--page: #f6f8f5;
--ink: #12211a;
--muted: #3d5148;
--panel: #ffffff;   /* soft green panel: #e2f0e6 */
--green: #1c5c3a;   /* buttons, accents (AA on white) */
--green-hover: #14432a;
--border: rgba(18,33,26,0.10);
```
Light mode is applied via `html[data-theme='light']` overrides in `snippets/tw-theme-mode.liquid`, `sections/tw-lightmode.liquid`, `sections/tw-lightmode-pages.liquid`. Any new section must get light-mode rules too.

## Typography

```css
font-family: -apple-system, 'Inter', BlinkMacSystemFont, sans-serif;
```
- Headlines: weight 800–900, letter-spacing -2px to -3px, line-height 0.95–1.05
- Headline accent line: gradient `linear-gradient(135deg,#2f8f5b,#4fbe80,#6fd699)` clipped to text
- Body: weight 400, line-height 1.6–1.65
- Eyebrows/tags: weight 700, uppercase, letter-spacing 2–2.5px, 11–13px
- Buttons: weight 700, letter-spacing -0.3px

## Logo

"Temply" in foreground color + "works" in green `#2f8f5b`, no space, weight 800. Green favicon/mark `templyworks-favicon-tw-green.png`.

## Product Naming Convention

`[Name] — Notion [Category] for [Audience]`
Examples: "Finance HQ — Notion Personal Finance Dashboard", "Client Pipeline — Notion CRM for Freelancers"

## Pricing Display

- Templates: `$19` (shown converted to local currency; use Liquid `money_with_currency`, never hardcode)
- Bundles: strikethrough compare-at + real price + savings
  Example: ~~$57~~ **$44** `Save 23%`
- Custom: "from $149"

## Component Patterns

**Eyebrow pill:**
```css
background: rgba(47,143,91,0.12);
border: 1px solid rgba(47,143,91,0.3);
border-radius: 100px;
padding: 6px 16px;
color: #4fbe80;
```

**Primary button:**
```css
background: #2f8f5b;
color: #fff;
border-radius: 10px;
padding: 16px 36px;
font-weight: 700;
```
Hover: `background: #1c5c3a; transform: translateY(-2px);`

**Ghost button:** transparent, `border: 1px solid rgba(255,255,255,.15)`, text `rgba(255,255,255,.6)`.

**Card:**
```css
background: rgba(255,255,255,0.028);
border: 1px solid rgba(255,255,255,0.075);
border-radius: 16px;
padding: 30px;
```
Hover: `border-color: rgba(79,190,128,0.45); transform: translateY(-5px);`

**Performance rules:** no `filter: blur()` on big elements, no `mix-blend-mode`, no `background-attachment: fixed` — they cause mobile lag/scroll problems. Use radial gradients instead.

## Tone Examples

✅ "Stop building Notion from scratch."
✅ "We turn chaos into systems."
✅ "Get instant access."
❌ "Unlock your productivity potential!"
❌ "Transform your workflow today!"
❌ Excessive emoji or exclamation points
