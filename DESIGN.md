# C2Coder design system - "build log"

Reference for reusing this visual language on other C2Coder properties (starting with `photo.c2coder.eu`). The canonical, working implementation is `assets/css/site.css` in this repo - copy that file as the starting point rather than re-deriving values from this doc.

## Concept

The site is styled like a maker's engineering logbook / schematic sheet, not a generic SaaS portfolio. Every recurring device on the page ties back to that idea:

- Grid-paper background (graph paper).
- A masthead ruled with a double line, like the top of a lab notebook page.
- Section labels and nav items in monospace, uppercase, letter-spaced - like stencil/silkscreen text on a PCB.
- Numbered nav (`01 Home`, `02 Projects` …) - the number encodes real reading order, not decoration.
- Projects presented as dated "log entries" (`LOG 001`), not marketing cards.
- Skills/gear presented as an "inventory" list (category → itemized row), like a parts sheet.
- Contact presented as a terminal/console panel with `$ ` prompts.

When adapting this for the photography site, keep the logbook conceit but swap the vocabulary to fit: e.g. photo sets as `ROLL 001` / `SET 001` entries, camera gear as the "inventory," an EXIF-style spec box next to a hero image instead of the "focus areas" box. Don't reuse "LOG" literally if it doesn't fit - the pattern matters more than the label.

## Color

Two themes, same tokens, swapped values. Single accent only - do not introduce a second hue.

| Token | Light | Dark | Use |
|---|---|---|---|
| `--paper` | `#f2f4f1` | `#0d1113` | Page background |
| `--ink` | `#12181c` | `#e7ebe8` | Primary text, borders, button fills |
| `--ink-soft` | `#4c555c` | `#a9b1ad` | Body copy |
| `--ink-faint` | `#7e858b` | `#626b67` | Meta text, labels, placeholders |
| `--line` | `#ccd2cf` | `#262c2a` | Hairline rules, grid lines |
| `--accent` | `#bf5b2a` | `#e08a4f` | Copper - links, tags, active state, one accent only |
| `--accent-contrast` | `#fdf7f0` | `#17110b` | Text on top of a solid `--accent` fill |
| `--console-bg` / `--console-ink` / `--console-accent` | dark panel on light page | light panel on dark page | The terminal/contact block always inverts against the page so it reads as a distinct "screen" |

Theme switching: `data-theme="dark"` / `data-theme="light"` on `<html>`, set on load from `localStorage` or `prefers-color-scheme`, toggled by a button whose label is the *target* theme (`DARK` shown in light mode, `LIGHT` shown in dark mode) - see the `themeToggle` script in any template.

The accent is a "copper/solder" orange - grounded in the electronics subject matter. If the photography site wants its own identity within the same system, it's fine to pick a different single accent hue (e.g. a darkroom red), but keep it to one accent, chosen deliberately, not a default blue/purple.

## Typography

- **Roboto** (400/500/700/900) - all prose, headings, buttons.
- **Roboto Mono** (400/500/700) - every label: nav, section tags, tags/chips, spec keys, terminal text, meta lines, footer.
- Load both from Google Fonts as one `<link>` (see `<head>` in any template).
- Headings use weight 900, `letter-spacing: -.01em`, `text-wrap: balance`.
- Mono labels are always uppercase with `letter-spacing: .04em`–`.14em`.
- Body copy max width ~58–65ch (`.hero-body`, `.prose-section p`).

## Layout primitives

- `.wrap` - max-width 1180px content column, 28px side padding. Everything lives inside it.
- `body` background is a 40×40px two-axis linear-gradient grid using `--line` - this is what gives the "graph paper" feel. Keep it subtle; it's a 1px hairline, not a visible grid image.
- Sections (`section`) get generous vertical rhythm (88px desktop / 60px mobile) and a `border-bottom: 1px solid var(--line)` - panels don't float, they're ruled off like notebook pages.
- No rounded corners anywhere, no drop shadows, no card-grid layouts. Borders are 1px solid (or 1px dashed for internal subdivisions like `.spec-row`), hard corners throughout.

## Components (class names from `site.css`)

- **Masthead** (`.masthead`, `.masthead-row`, `.masthead-nav`, `.ctrl-btn`) - sticky, double-ruled bottom border, numbered nav, two text-button controls (theme + mobile menu).
- **Mobile nav** (`.nav-overlay`) - full-screen takeover, not a dropdown. Big mono links, same numbering as desktop nav.
- **Hero** (`.hero-grid`, `.spec-box`) - headline + body on the left (never centered), a bordered "spec box" datasheet-style aside on the right listing 2–4 key facts.
- **Log entry** (`.log-entry`, `.log-id`, `.chip`, `.entry-link`) - two-column row: an id/tags meta column, then title + description + link. Used for the projects list.
- **Status badge** (`.status-badge`, `.is-wip`) - outlined by default, solid-filled for `wip`. Use sparingly for real state, not decoration.
- **Inventory row** (`.inv-row`, `.inv-key`, `.inv-val`) - label/value definition-list row, values joined with ` · `. Used for skills/gear/setup lists.
- **Terminal panel** (`.term-panel`, `.term-bar`, `.term-line`, `.prompt`, `.cursor-blink`) - inverted console block for contact info, `$ ` prompt prefix per line, optional blinking cursor on the last line (respects `prefers-reduced-motion`).
- **Buttons** (`.btn-solid`, `.btn-line`) - mono, uppercase, hard-cornered, 1px border. Solid = accent fill for the primary action; outline for secondary.
- **Project/detail page** (`.back-link`, `.project-head`, `.project-grid`, `.prose-section`, `.file-row`) - same masthead/footer chrome, a summary + tag row up top, a two-column body (prose sections left, spec box + downloadable-files box right).

## Content patterns worth reusing

- **Numbered nav is literal reading order.** Don't add numbers elsewhere unless they encode something equally real (a real sequence, a real id).
- **Files, not just links.** When something isn't hosted on GitHub, give it its own page (`/projects/<slug>/`) with a `.file-row` list pointing at static files under `assets/projects/<slug>/` rather than faking a repo link.
- **WIP is a real status, not flavor text.** Only use the badge when something is genuinely unfinished, and remove it the day it's done.

## Applying this to the photography site

1. Copy `assets/css/site.css` wholesale as the starting token/component set.
2. Keep the masthead, numbered nav, mobile overlay, and terminal-contact pattern as-is - they're identity, not implementation detail.
3. Replace `.log-entry` (projects) with a photo-set/roll listing using the same two-column meta+content shape.
4. Replace `.inv-row` (skills/setup) with camera/lens/gear inventory - it's already a label→value list, which is exactly what gear specs are.
5. Decide deliberately whether to keep the copper accent (shared identity across c2coder.eu properties) or pick one new accent hue for photography - don't default to blue.
6. Keep the structure single-language (English) at the root the same way this repo does it - no locale prefixes, no language switch in the nav.
