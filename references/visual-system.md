# Fixed visual system

`assets/reference-casebook.html` is the canonical layout and implementation reference. Copy and adapt it; do not redesign it.

## Visual identity to preserve

- warm paper background with subtle green and orange radial washes;
- dark ink typography, forest green primary accent, burnt orange risk accent, muted blue and purple secondary accents;
- Georgia/Songti-style editorial display headings with system sans-serif body text;
- sticky translucent top navigation;
- oversized editorial hero and four evidence-count statistics;
- dark green summary panel with three takeaway columns;
- rounded paper cards with restrained borders and shadows;
- orange reviewer panels, blue rebuttal panels, green implication panels;
- circular relevance badge and compact score dots;
- generous whitespace and no decorative stock imagery.

## Interaction model to preserve

- keyword search over all paper-card text;
- topic filter chips;
- per-paper details expander with correct `aria-expanded` state;
- anchor navigation to conclusion, cases, pre-review, and rebuttal guidance;
- print stylesheet that exposes details and removes interactive controls;
- responsive single-column layouts at narrow widths.

## Allowed changes

- titles, counts, section prose, paper cards, tags, colors assigned to semantic tags, and official links;
- the number of paper cards and anticipated reviewer questions;
- bilingual labels when required by the user.

## Disallowed drift

- no React/Vue build, package manager, backend, or online deployment requirement;
- no external font, icon, CSS, or JavaScript dependency;
- no generic dashboard layout, dense spreadsheet-like table, or dark-mode redesign;
- no removal of source disclosure, missing-rebuttal notices, search, filters, details, responsive CSS, or print CSS;
- no placeholder statistics or fabricated review evidence.

## Responsive targets

- Desktop: three-column concern/response/lesson panels and four-column summary grids.
- Tablet: stacked paper analysis panels and two-column supporting grids.
- Mobile (approximately 390 px wide): one column, hidden top navigation, readable buttons, no horizontal scrolling.

The finished page should look like an editorial research dossier, not a software admin console.
