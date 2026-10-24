# Research protocol

Use this protocol to build the evidence set before writing the casebook.

## 1. Translate the project into similarity axes

Choose 3–5 dimensions that explain why another paper is useful. Typical axes:

- research object: benchmark, model, training objective, explanation method;
- construct: faithfulness, grounding, robustness, hallucination, causal sensitivity;
- intervention: counterfactual image, feature ablation, masking, restoration, prompt or reasoning intervention;
- modality/domain: medical images, general vision-language, language reasoning;
- contribution type: diagnostic benchmark, mitigation method, or both.

Prefer a diverse case set that covers the user's likely reviewer attacks. Do not select five papers that all teach the same lesson.

## 2. Source hierarchy

Use sources in this order:

1. Official OpenReview forum and its review, author response, meta-review, and decision notes.
2. Official conference proceedings or project page for paper metadata and final version.
3. Public structured mirrors of OpenReview records when the official site is technically inaccessible.
4. arXiv or institutional repositories for the paper text.

Search snippets, blog summaries, and AI-generated paper summaries may help discovery but must not be the evidence for reviewer or rebuttal claims.

## 3. Extraction record

For every candidate, record:

- official title, venue, year, decision, and forum URL;
- why it is similar to the user's work;
- every available review score and confidence;
- 3–5 decision-relevant concerns, attributed to reviewers;
- the author's concrete response to each concern;
- new experiments, metrics, data, definitions, or revisions added during rebuttal;
- final justification or meta-review, when present;
- whether a rebuttal is absent from the consulted public record.

Retain raw notes outside the final HTML when practical so claims can be audited.

## 4. Synthesis rules

- Combine duplicate reviewer concerns but retain meaningful disagreement.
- Minor typos belong only in detailed notes when they affected the review outcome.
- Quote no more than a short phrase; paraphrase the rest.
- A score increase is relevant only when the review or meta-review connects it to the response.
- “Accepted” does not mean every concern was resolved.
- When a reviewer challenges causal terminology, report the exact construct-validity issue rather than softening it to “needs more experiments.”

## 5. Selection check

The final set should normally include:

- one paper closest to the benchmark contribution;
- one closest to the proposed method;
- one domain-specific benchmark or medical evaluation paper;
- one direct explanation/faithfulness/counterfactual paper;
- one useful contrast case exposing release, scale, judge, or presentation risks.

If the field lacks public rebuttals, say so and include the best adjacent cases rather than pretending exact matches exist.
