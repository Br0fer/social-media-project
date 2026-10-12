---
name: Social Media
description: A Django social network where every surface wears the solid colour of the space it belongs to.
colors:
  people: "#3d7a22"
  people-soft: "#e3f0d8"
  people-deep: "#1f4a1c"
  groups: "#0f766e"
  groups-soft: "#d5efec"
  groups-deep: "#134e4a"
  channels: "#8b3f8f"
  channels-soft: "#f3e3f2"
  channels-deep: "#5b2160"
  on-color: "#ffffff"
  ground: "#f1f5ec"
  ground-deep: "#e4ecdb"
  surface: "#ffffff"
  surface-sunk: "#f7faf3"
  line: "#d3e0c7"
  line-strong: "#b3c8a2"
  ink: "#1a2617"
  ink-strong: "#1f4a1c"
  ink-muted: "#53664d"
  ink-faint: "#748a6d"
  danger: "#dc2626"
  danger-soft: "#fee2e2"
  success: "#15803d"
  success-soft: "#dcfce7"
  warning: "#b45309"
  warning-soft: "#fef3c7"
typography:
  display:
    fontFamily: "Unbounded, Inter, system-ui, sans-serif"
    fontSize: "clamp(1.875rem, 1.3rem + 2.4vw, 3rem)"
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Unbounded, Inter, system-ui, sans-serif"
    fontSize: "clamp(1.5rem, 1.2rem + 1.2vw, 2rem)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Unbounded, Inter, system-ui, sans-serif"
    fontSize: "1.5625rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  title-sm:
    fontFamily: "Unbounded, Inter, system-ui, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "-0.02em"
  body:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.55
    fontFeature: "\"cv11\", \"ss01\""
  body-long:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 600
    lineHeight: 1
  caption:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 400
    lineHeight: 1.35
rounded:
  sm: "10px"
  md: "14px"
  lg: "22px"
  xl: "32px"
  pill: "999px"
  leaf: "46% 14% 46% 14%"
  pebble: "58% 42% 52% 48% / 48% 56% 44% 52%"
spacing:
  s-1: "4px"
  s-2: "8px"
  s-3: "12px"
  s-4: "16px"
  s-5: "24px"
  s-6: "32px"
  s-7: "48px"
  s-8: "64px"
components:
  button-primary:
    backgroundColor: "{colors.people}"
    textColor: "{colors.on-color}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0 20px"
    height: "44px"
  button-soft:
    backgroundColor: "{colors.people-soft}"
    textColor: "{colors.people-deep}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0 20px"
    height: "44px"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0 20px"
    height: "44px"
  button-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-color}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0 20px"
    height: "44px"
  button-on-block:
    backgroundColor: "{colors.on-color}"
    textColor: "{colors.people}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0 20px"
    height: "44px"
  button-sm:
    rounded: "{rounded.pill}"
    padding: "0 14px"
    height: "36px"
  button-lg:
    rounded: "{rounded.pill}"
    padding: "0 28px"
    height: "52px"
  reaction:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0 16px"
    height: "44px"
  reaction-like-on:
    backgroundColor: "{colors.channels-soft}"
    textColor: "{colors.channels-deep}"
  reaction-repost-on:
    backgroundColor: "{colors.groups-soft}"
    textColor: "{colors.groups-deep}"
  chip:
    backgroundColor: "{colors.people-soft}"
    textColor: "{colors.people-deep}"
    rounded: "{rounded.pill}"
    padding: "0 10px"
    height: "26px"
  block:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "24px"
  post-origin-strip:
    backgroundColor: "{colors.people}"
    textColor: "{colors.on-color}"
    padding: "12px 16px 12px 12px"
  space-hero:
    backgroundColor: "{colors.people}"
    textColor: "{colors.on-color}"
    rounded: "{rounded.xl}"
    padding: "64px 32px 32px"
  welcome-browse-tile:
    backgroundColor: "{colors.people}"
    textColor: "{colors.on-color}"
    rounded: "{rounded.lg}"
    padding: "18px 20px"
    height: "132px"
  empty-state:
    textColor: "{colors.ink-muted}"
    rounded: "{rounded.lg}"
    padding: "48px 24px"
  input:
    backgroundColor: "{colors.surface-sunk}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
    height: "48px"
  input-focus:
    backgroundColor: "{colors.surface}"
  nav-item:
    textColor: "{colors.ink-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0 14px"
    height: "40px"
  nav-item-active:
    backgroundColor: "{colors.people-soft}"
    textColor: "{colors.people-deep}"
  pager-current:
    backgroundColor: "{colors.people}"
    textColor: "{colors.on-color}"
    rounded: "{rounded.pill}"
    height: "44px"
  toast:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "12px 12px 12px 16px"
  sheet:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.xl}"
    width: "min(520px, calc(100vw - 32px))"
---

# Design System: Social Media

## Overview

**Creative North Star: "Three Coloured Rooms"**

The app is a house with three rooms, and each room is painted one solid colour taken from the outdoors: people are fern green, groups are lake teal, channels are heather. Every post, header, directory entry and nav item announces which room it belongs to through a full-strength block of that colour, so a reviewer always knows whether they are acting on a person, in a group or in a channel. Fern doubles as the brand, because the default room is your own profile.

Around those blocks the world is calm and natural: a pale moss-tinted paper ground with a faint fractal grain, white content blocks with generous 22px corners, chunky pill buttons, and soft forest-tinted shadows that sit with a real downward offset. The forms are organic: group and channel pictures are leaves, the space headers carry terrain contour lines, and the wordmark is three leaf blades. Headings speak in Unbounded, wide and heavy; everything else is Inter. Dark mode follows the OS and swaps the paper for deep forest-black, lifting the three space colours for contrast while keeping their identity.

Motion is quick and physical: custom ease-out curves, a slight scale on press, toasts and dialogs that enter from `@starting-style`, short staggered feed entrance, and cross-document view transitions that keep the top bar still. All of it collapses under `prefers-reduced-motion`.

**Key Characteristics:**
- One space, one colour, at full strength (fern people, lake-teal groups, heather channels).
- Colour is scoped, never hard-coded: components read `--space*` variables and a `.space-person` / `.space-group` / `.space-channel` ancestor decides the room.
- White blocks on grained moss paper, 22px corners, soft forest-tinted offset shadows.
- Leaf-shaped pictures for groups and channels, circles for people; terrain contours in space headers.
- Unbounded 700-800 headings, Inter body, Bootstrap Icons line icons.
- Pill controls with 44px minimum touch height and a 0.97 press scale.
- Light and dark from the OS; the space colours survive both.

## Colors

A nature palette: three saturated outdoor colours on a green-leaning neutral family; every neutral leans toward moss and forest so the paper, the hairlines and the ink belong to the same world.

### Primary
- **People Fern** (`people`): the people space and the brand. Origin strips on profile posts, the profile hero, the "New post" pill, the mobile "Post" tab, the wordmark's first bar, the status-page numerals, focus rings and selection on person-scoped pages. Its soft tint (`people-soft`) backs chips, active nav items and soft buttons; its deep shade (`people-deep`) is the text on those tints.

### Secondary
- **Groups Lake Teal** (`groups`): the group space. Group origin strips, the group hero, group directory monograms, the active "Groups" nav item, and the repost reaction once it is on. Info toasts borrow it too. Same soft/deep pairing as fern.

### Tertiary
- **Channels Heather** (`channels`): the channel space. Channel origin strips, the channel hero, channel monograms, the active "Channels" nav item, and the like reaction once it is on. Same soft/deep pairing.

### Neutral
- **Moss Paper** (`ground`): the page ground and the light `theme-color`. The top bar is this colour at 86% over a 14px backdrop blur.
- **Deeper Moss** (`ground-deep`): nav hover fill.
- **White Block** (`surface`): every content block, card, menu, toast and dialog.
- **Sunk Field** (`surface-sunk`): input fields at rest, media wells, the article action bar.
- **Lichen Hairline** (`line`) and **Sage Rule** (`line-strong`): block edges and dividers; the stronger rule marks hover edges, dashed empty states and file inputs.
- **Forest Ink** (`ink`): body text. **Pine Ink** (`ink-strong`): headings. **Sage** (`ink-muted`): secondary text, meta, counts, field icons. **Faint Sage** (`ink-faint`): placeholders and the search-field icon only.
- **State colours** (`danger`, `success`, `warning`, each with a `-soft` tint): toasts, destructive buttons, the confirm icon and form errors. They never stand in for a space.

### Dark theme
Follows `prefers-color-scheme` (and a `data-theme="dark"` override). Ground becomes forest-black (the dark `theme-color`), surfaces become dark moss, and each space splits in two: a lifted tone for text, links, buttons and focus (people `#93c972`, groups `#5ec4b8`, channels `#cf9ad2`, with forest-black ink on them) and a deep **block** tone for solid colour fields (people `#2f6619`, groups `#0d5e57`, channels `#6e2f73`, with white on them). Full dark values live in `.impeccable/design.json`.

### Named Rules
**The One Room, One Colour Rule.** A surface takes the colour of the space it belongs to and no other. Set the room with a `.space-person`, `.space-group` or `.space-channel` scope and let components read `--space`, `--space-soft`, `--space-deep` and `--space-block`; never hard-code a space hex inside a component.

**The Full Strength Rule.** Where a surface names its space (origin strip, hero, monogram, welcome tile), the colour is a solid block at full strength, using the block tone, with white text. Tints are for controls and states, not for identifying a space.

**The Block Tone Rule.** Solid colour fields (origin strips, heroes, monograms, avatar fallbacks, welcome tiles) use the block tone in both themes, so one space is one colour everywhere; lifted tones are only for text-scale and control-scale use.

## Typography

**Display Font:** Unbounded (with Inter, system-ui)
**Body Font:** Inter (with system-ui, -apple-system, Segoe UI, Roboto)

**Character:** Unbounded is wide, round and loud, which is what makes a block of colour feel like a sign; Inter keeps the reading text quiet and handles Cyrillic cleanly, so Ukrainian strings sit as well as English ones.

### Hierarchy
- **Display** (800, 1.875-3rem fluid, 1.15): page `h1`, hero names, the feed title. Tight -0.02em tracking, balanced wrap.
- **Headline** (700, 1.5-2rem fluid, 1.15): `h2`, form and article titles.
- **Title** (700, 1.5625rem, 1.15): section titles, comment headers, dialog titles, confirm titles.
- **Title Small** (700, 1.25rem, 1.3): post titles in the feed (coloured with the space's deep tone), directory entry names, empty-state headings.
- **Body** (400, 1rem, 1.55): all running text, with Inter's `cv11` and `ss01` features on. Article text steps up to 1.125rem / 1.65 at 70ch.
- **Label** (600, 0.875rem, 1): buttons, nav items, reactions, field labels. Not uppercase, no tracking.
- **Caption** (400-600, 0.8125rem): timestamps, helper text, counts. Numbers use tabular figures.

### Named Rules
**The Two Voices Rule.** Unbounded is for headings, the wordmark, avatar initials, hero stats, monograms and welcome-tile labels; Inter is for everything a person reads or presses. No third family.

**The Room for Ukrainian Rule.** Headings and paragraphs wrap with `overflow-wrap: anywhere` and balanced/pretty wrapping; never size a control or heading to fit an English string exactly.

## Layout

A centred 1240px page with 24px side padding (16px on phones). The signed-in feed is a three-column shell: a 280px left rail (your profile block and shortcuts), a 640px feed column, and a 280px right rail (create actions and the colour legend), 32px apart. Rails are sticky under the 64px top bar. At 1180px the right rail drops; at 860px the shell becomes one column, the top-bar nav hides and a fixed five-slot bottom tab bar takes over, with a fern "Post" pill in the centre slot. Space pages (profile, group, channel) put a full-width hero above a 640px feed column. Forms sit in a 640px column, confirmations in 480px, status pages in 560px. The signed-out welcome is an 880px block.

Spacing follows an 8px-based scale (4, 8, 12, 16, 24, 32, 48, 64). Feed items are 24px apart; grids and stacks use 16px. Directories auto-fill at 340px minimum; the people grid auto-fills at 220px and becomes a single divided list under 640px. The welcome browse tiles sit in three equal columns 14px apart and stack into full-width rows under 560px.

## Elevation & Depth

Depth is a soft shadow with a real downward offset, tinted forest green in light mode and pure black in dark mode. Under it the ground is a material, not a flat fill: in light theme the body carries a tiled 180px SVG fractal-noise grain (`--grain`, forest-tinted at about 7% alpha), barely visible, so the page reads as paper; dark theme drops the grain and stays a clean forest-black. Space heroes carry a second texture, terrain contour lines (`--contours`, an inline SVG of white 1.4px strokes: a nested ring of elevation lines and three ridge lines along the bottom), sized to cover, anchored right, at 0.22 opacity and masked in from the right (`linear-gradient(100deg, transparent 20%, #000 70%)`). Content blocks sit at level 2 at rest, so they visibly lift off the paper rather than being outlined by a hairline. Overlays (menus, toasts, dialogs) sit at level 3 and drop their border: elevation alone defines them. The dialog backdrop is a translucent forest-black with a 3px blur.

### Shadow Vocabulary
- **Level 1** (`--shadow-1`): primary button at rest.
- **Level 2** (`--shadow-2`): every content block (posts, entries, people, blocks), heroes, hover lift on primary buttons and welcome tiles.
- **Level 3** (`--shadow-3`): user menu, toasts, dialogs.
Exact values for both themes are in `.impeccable/design.json`.

### Named Rules
**The Soft Offset Rule.** Shadows are blurred, layered and offset downward; never a hard, unblurred offset shadow.

**The Borderless Overlay Rule.** Anything floating above the page (menu, toast, dialog) has no visible border; its shadow is the edge.

**The Quiet Texture Rule.** Texture lives in two places only: the paper grain on the light-theme ground and the contour lines on space heroes. Both stay faint (grain about 7% alpha, contours 0.22 opacity) and sit behind content; never put texture on content blocks, controls or text.

## Shapes

Generous, friendly rounding at every scale, with an organic second vocabulary for anything that pictures a space. Corners: 10px for menu items, 14px for inputs, comments and toasts, 22px for content blocks, empty states and welcome tiles, 32px for heroes and dialogs (heroes drop to 22px under 600px), full pills for every button, chip, reaction, top-bar nav item and pager link.

The organic forms:
- **Leaf** (`rounded.leaf`, 46% 14% 46% 14%): two generously rounded corners opposite two tight ones. It is the shape of a group or channel picture wherever one appears (post-origin avatars, hero pictures, the 64px directory monograms) and of the icon swatches that stand for a space (the 34px rail-link swatches and the 40px welcome-tile swatches). People pictures stay circles, so the silhouette repeats the space distinction.
- **Leaf blade** (8px 2px 8px 2px): the three staggered 8x22px bars of the wordmark, in fern, lake teal and heather.
- **Pointed leaf** (100% 0 100% 0): the empty-state sprout, three 20px leaves at 30, 46 and 26px tall, the outer two tilted -12 and 12 degrees; the welcome page's tall background leaves use the same shape stretched (100% 0 100% 0 / 60% 0 60% 0).
- **Pebble** (`rounded.pebble`, 58% 42% 52% 48% / 48% 56% 44% 52%): the soft irregular stones drifting behind the sign-in and register art, alongside one leaf.

### Named Rules
**The Leaf Is a Space Rule.** The leaf shape belongs to space pictures: group and channel avatars, monograms and hero pictures, plus the icon swatches that stand for a space. A person's picture is always a circle, and controls, blocks and fields never take the leaf.

## Components

### Buttons
Chunky, confident pills that answer the press.
- **Shape:** full pill, 44px tall (36px small, 52px large), 1.5px border, Inter 600 label, optional leading icon.
- **Primary:** space colour fill with on-space text and level 1 shadow; hover lifts to level 2 with a slight brightness bump.
- **Soft:** space tint with deep text; hover draws the border in the space colour.
- **Ghost:** transparent with a hairline; hover fills white with the stronger rule. A danger ghost variant uses danger text and a danger-tint hover.
- **Danger:** solid danger fill for confirmed destructive actions only.
- **On-block / Outline-on-block:** white fill with block-colour text, or a translucent white outline, for actions inside a coloured hero.
- **Press / Busy:** scale 0.97 on `:active` (160ms ease-out); busy buttons dim to 75% and show a 14px spinning ring.

### Reactions
Like and repost are pill toggles with a count. Off: white with a hairline and sage text. On: like turns heather-tinted, repost turns lake-teal-tinted, with the icon in the full colour. Press scales the pill to 0.95 and the icon to 0.8.

### Chips
Small 26px pills naming a space ("Group", "Channel") with an icon: space tint with deep text by default, solid space colour, or translucent white when sitting on a coloured strip or hero.

### Cards / Containers
- **Corner Style:** 22px.
- **Background:** white block on moss paper.
- **Shadow Strategy:** level 2 at rest, with a hairline edge that strengthens (or turns the space colour on directory and people cards) on hover.
- **Internal Padding:** 24px (16px for directory entries, 32px for form cards).

### Post Block (signature)
A white block that opens with an **origin strip** in the space's solid block colour: avatar (leaf for groups and channels, circle for people), name and timestamp in white, and a translucent space chip on the right. Below it: optional media in a sunk well, the title in Unbounded tinted with the space's deep tone, a three-line excerpt, and a stats row (likes, reposts, comments) whose "Read" link slides in on hover. The whole block is the link target.

### Space Hero (signature)
The header of every profile, group and channel: a 32px-radius slab of the space's block colour (or the banner image under a scrim fading into it), white terrain contour lines at 0.22 opacity masked in from the right, a 128px picture with a 5px white ring (a circle on profiles, a leaf on groups and channels), the name in Display, white stats in Unbounded numerals, and an action bar along the bottom on a 14% dark tint. Actions inside use the on-block button variants.

### Welcome Browse Tiles (signature)
The signed-out welcome ends in three solid tiles, one per space (groups, channels, people), each scoped to its room and filled with that space's block colour. They sit below a hairline in a three-column grid, 14px apart. Each tile is 22px-radius, at least 132px tall, padded 18px 20px, and spreads its content top to bottom: a 40px leaf-shaped icon swatch (white at 20%) holding a Bootstrap line icon, then an Unbounded 700 1rem label in white with a small Inter 500 caption under it at 82% white. On hover-capable pointers a tile lifts 2px and gains level 2 (200ms ease-out); press scales to 0.97. Under 560px the tiles stack into full-width rows with the swatch beside the text.

### Inputs / Fields
- **Style:** 48px tall, 14px radius, 1.5px lichen hairline, sunk-field background, Inter 1rem; labels above in Inter 600 0.875rem.
- **Focus:** border turns the space colour, background turns white, and a 4px halo of the space colour at 18% appears.
- **Error:** danger border with a danger message list above the field; non-field errors sit in a danger-tint panel. File inputs are dashed with a soft pill selector button.

### Navigation
Top bar: sticky, 64px, translucent paper with blur, the three-blade wordmark on the left. Nav items are 40px pills in sage; each carries its own space scope, so the active item fills with its room's tint and deep text (Groups goes lake teal, Channels heather). On the right: a ghost icon button for requests, the fern "New post" pill, and the avatar opening a borderless level 3 menu that pops in from the top right. Under 860px the bottom tab bar shows icon-over-label tabs in sage, the active tab in its space colour.

### Feedback
- **Toasts:** top-right stack (full width on phones), white, 14px radius, level 3, with a tinted 28px icon tile in the tone colour; they slide in from `@starting-style`, pause on hover or focus, and slide right to leave.
- **Dialog sheet:** centred, 32px radius, scales in from 0.96 over a blurred forest-black backdrop; on phones it becomes a bottom sheet that rises with the drawer curve.
- **Confirm page:** a centred block with a 64px tinted icon tile (danger, or the space tint for non-destructive confirms) and equal-width paired buttons.
- **Empty state:** dashed 2px rule at 22px radius, a three-leaf sprout in the space colour as art, Title Small heading and a short line.

## Do's and Don'ts

### Do:
- **Do** wrap every surface in the scope of its space (`.space-person`, `.space-group`, `.space-channel`) and let components read `--space*` variables.
- **Do** mark where a post or page lives with a full-strength block of its space colour, using the block tone so it matches in light and dark.
- **Do** size standard buttons, reactions, pager links and menu rows at 44px (small buttons 36px, top-bar nav pills 40px) and give pressable controls the press scale (0.95-0.97) with `cubic-bezier(0.23, 1, 0.32, 1)`.
- **Do** use the soft forest-tinted offset shadows (level 2 for content, level 3 for overlays) and drop the border on overlays.
- **Do** give group and channel pictures and space swatches the leaf shape (`--leaf`), and keep people pictures circular.
- **Do** use Bootstrap Icons line glyphs, `aria-hidden`, beside a visible or screen-reader label.
- **Do** guard every animation with `prefers-reduced-motion` and hover effects with `(hover: hover) and (pointer: fine)`.
- **Do** use tabular figures for counts and stats.

### Don't:
- **Don't** let one space's colour identify another space's surface; fern on a group header or a heather strip on a profile post breaks the reading of the whole app. The fixed-colour exceptions in the build are reaction states (like heather, repost lake teal) and info toasts (lake teal).
- **Don't** use a pale tint where the build uses a solid block to name a space (origin strips, heroes, monograms, welcome tiles).
- **Don't** add a hard, unblurred offset shadow; depth here is always soft.
- **Don't** introduce a third typeface or set body text in Unbounded.
- **Don't** use the state colours (danger, success, warning) to identify a space, or a space colour to signal an error.
- **Don't** use square corners on controls; buttons, chips, reactions, top-bar nav items and pager links are pills, and list rows inside blocks round at 10-14px.
