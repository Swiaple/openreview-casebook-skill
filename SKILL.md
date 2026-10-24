---
name: openreview-casebook
description: Research papers similar to a user's project, analyze public peer-review discussions and author rebuttals, and produce a polished standalone HTML casebook with a fixed editorial visual system. Use when the user wants comparable OpenReview cases, reviewer concerns, rebuttal lessons, or a submission-focused literature review in HTML. Do not use for ordinary literature searches that do not require peer-review analysis or for non-HTML reports.
---

# OpenReview Casebook

Create an evidence-backed peer-review casebook that helps the user understand how adjacent work was challenged, how authors responded, and what those records imply for the user's own research. Preserve the reference casebook's analysis depth, editorial structure, visual language, and offline interactivity while replacing its subject matter.

## Inputs and defaults

The user only needs to identify their research topic or say what kind of work should be considered similar. Infer reasonable search dimensions from the supplied project context. Ask a question only when the topic itself or the intended comparison is genuinely ambiguous.

Default to:

- 5–7 strongly related papers, prioritizing accepted papers with public reviews and rebuttals;
- recent major conferences or journals, plus an older paper only when it is foundational;
- an offline, single-file HTML deliverable in the current workspace;
- Chinese editorial prose when the user writes in Chinese, while preserving official English paper titles and venue names.

## Required workflow

1. Read [references/research-protocol.md](references/research-protocol.md) before searching.
2. Define 3–5 similarity axes from the user's project, such as benchmark design, intervention type, modality, domain, faithfulness construct, or training method. Select papers for conceptual usefulness, not keyword overlap alone.
3. Collect primary-source paper metadata and public peer-review records. Prefer official OpenReview pages and conference proceedings. A public structured mirror may be used when direct OpenReview access is blocked, but link every case back to its official forum.
4. Separate four evidence types in notes:
   - claims from the paper;
   - reviewer concerns;
   - author rebuttal or revision evidence;
   - this casebook's implications for the user's work.
5. Never infer an author response from the final paper or acceptance decision. If the public record does not contain a rebuttal, label it clearly as unavailable in the consulted record.
6. Read [references/content-model.md](references/content-model.md), then synthesize the casebook. Paraphrase rather than copying long review passages. Preserve concrete details such as sample counts, new ablations, judge agreement, score changes, or metric values when they explain why a response worked.
7. Copy `assets/reference-casebook.html` to the requested output and adapt its content in place. The asset contains fictional examples only; replace every example title, review, response, implication, score, statistic, tag, and source placeholder with verified material for the current request. Preserve its visual system and interaction model as defined in [references/visual-system.md](references/visual-system.md). Do not rebuild the page with a different framework or external dependency.
8. Include all required sections:
   - hero and evidence counts;
   - a short overall conclusion;
   - recurring reviewer attack patterns;
   - searchable/filterable paper cards;
   - for every paper: reviewer concerns, author response status, implications, scores, official link, and expandable per-review notes;
   - a pre-review of the user's own project;
   - a practical rebuttal response structure;
   - source and methodology disclosure.
9. Run `scripts/validate_casebook.py OUTPUT.html`. Fix every reported error.
10. Preview the file in a local browser at desktop and narrow mobile widths. Test search, filter chips, one details expander, external links, and console errors. The file must remain usable when opened directly without a server.

## Analysis standard

- Lead with the reviewer concern that could change an accept/reject decision, not minor wording comments.
- Explain what evidence the author added, not merely that the author “clarified” something.
- Distinguish a rebuttal that resolved a concern from one that only narrowed the claim.
- Treat meta-review language and score changes as evidence of rebuttal effect, while avoiding causal certainty when the record is ambiguous.
- Convert each case into a concrete preparation item for the user's project: a control, ablation, external dataset, human audit, statistical test, wording change, or release artifact.
- Be especially strict about construct validity, data leakage, intervention artifacts, judge reliability, coverage/filtering bias, cross-dataset generalization, and claims of internal causality.

## Boundaries

- Do not bypass CAPTCHA, anti-bot checks, paywalls, or login controls.
- Do not invent missing reviews, rebuttals, score changes, acceptance rationales, or paper results.
- Do not present the casebook's recommendations as the cited paper's conclusions.
- Do not expose private drafts, credentials, or non-public reviews.
- Do not publish or upload the generated casebook unless the user separately authorizes that destination and visibility.
- Keep the page dependency-free: no external fonts, JavaScript libraries, analytics, or CDN assets.

## Delivery

Lead with the completed HTML file. Briefly state the number of papers and reviews covered, name the two most useful cases to read first, disclose any missing rebuttals, and link the primary public sources used.
