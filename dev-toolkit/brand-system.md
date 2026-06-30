# Brand System — TemplyWorks

## Identity

**Name:** TemplyWorks (always one word, capital T and W: "TemplyWorks")
**Tagline direction:** "Your freelance business, organized. Finally."
**Voice:** Direct, confident, productive. Not corporate, not hype-y. Real benefits over generic productivity-guru language.

## Colors

```css
--tw-bg: #080810;              /* primary background */
--tw-purple: #7c3aed;          /* primary accent */
--tw-purple-hover: #6d28d9;    /* hover state */
--tw-purple-light: #a78bfa;    /* secondary accent text */
--tw-purple-lighter: #c4b5fd;  /* tertiary, gradients */
--tw-purple-deep: #5b21b6;     /* darker accent variant */
--tw-text-primary: #ffffff;
--tw-text-muted: rgba(255,255,255,0.5);
--tw-text-faint: rgba(255,255,255,0.32);
--tw-border: rgba(255,255,255,0.08);
--tw-border-accent: rgba(124,58,237,0.18);
```

## Typography

```css
font-family: -apple-system, 'Inter', BlinkMacSystemFont, sans-serif;
```
- Headlines: weight 800-900, letter-spacing -2px to -3px, tight line-height (0.93-1.05)
- Body: weight 400, line-height 1.6-1.65
- Labels/eyebrows: weight 500-700, uppercase, letter-spacing 2-2.5px, small (11-13px)
- Buttons: weight 700, letter-spacing -0.2px to -0.3px

## Logo Treatment

"Temply" in white + "Works" in purple (`#7c3aed`), no space, single wordmark, weight 800.

## Product Naming Convention

`[Name] — Notion [Category] for [Audience]`
Examples: "Finance HQ — Notion Personal Finance Dashboard", "Client Pipeline — Notion CRM for Freelancers"

## Pricing Display Convention

- Individual templates: always show as `€9.99`
- Bundle: show strikethrough original + real price + savings badge
  Example: ~~€59.94~~ **€34.99** `Save 42%`

## Component Patterns

**Eyebrow/badge pill:**
```css
background: rgba(124,58,237,0.12);
border: 1px solid rgba(124,58,237,0.3);
border-radius: 100px;
padding: 6px 16px;
color: #a78bfa;
```

**Primary button:**
```css
background: #7c3aed;
color: #fff;
border-radius: 10px;
padding: 16px 36px;
font-weight: 700;
```
Hover: `background: #6d28d9; transform: translateY(-2px);`

**Card:**
```css
background: rgba(255,255,255,0.028);
border: 1px solid rgba(255,255,255,0.075);
border-radius: 16px;
padding: 32px;
```
Hover: `border-color: rgba(124,58,237,0.45); transform: translateY(-5px);`

## Tone Examples (for copy generation)

✅ "Stop building Notion from scratch."
✅ "I use these templates in my own work."
✅ "Get instant access."
❌ "Unlock your productivity potential!"
❌ "Transform your workflow today!"
❌ Excessive emoji or exclamation points
