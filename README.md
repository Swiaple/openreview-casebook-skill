# OpenReview Casebook Skill

A reusable Codex skill for finding papers adjacent to a research project, analyzing their public peer reviews and author rebuttals, and turning the evidence into a polished standalone HTML casebook.

The skill preserves a fixed editorial layout with interactive filters, expandable review notes, responsive design, and submission-focused analysis. Its bundled HTML asset contains fictional examples only and does not disclose any source project, unpublished work, or real paper-selection history.

## Use

Install the repository at:

```text
~/.codex/skills/openreview-casebook
```

Then invoke it with a request such as:

```text
Use $openreview-casebook to find work similar to my research project,
analyze the OpenReview comments and rebuttals, and create an offline HTML
casebook.
```

The user only needs to describe the research topic and what “similar work” means. The skill handles paper selection, source verification, review/rebuttal synthesis, project-specific pre-review, HTML generation, interaction checks, and responsive visual QA.

## Contents

- `SKILL.md` — routing, evidence standards, workflow, and delivery rules.
- `references/` — research protocol, content model, and fixed visual system.
- `assets/reference-casebook.html` — canonical standalone HTML reference.
- `scripts/validate_casebook.py` — offline structural validator for generated pages.
- `agents/openai.yaml` — Codex UI metadata and default invocation prompt.

## Design principles

- Primary sources first: official OpenReview and conference records.
- No invented rebuttals or inferred author responses.
- Reviewer concern, author response, and project-specific implication remain visibly separate.
- Standalone HTML with no external runtime dependencies.
- Desktop, mobile, print, search, filters, and detail expanders are verified before delivery.
