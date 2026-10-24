# Casebook content model

Use this as a completeness schema, not as a requirement to expose JSON in the final deliverable.

## Page-level fields

- `project_name`
- `casebook_title`
- `one_sentence_purpose`
- `paper_count`
- `review_count`
- `available_rebuttal_count`
- `risk_family_count`
- `overall_conclusion`
- `three_takeaways`
- `recurring_attacks`
- `anticipated_reviews_for_user_project`
- `rebuttal_response_steps`
- `sources_and_limitations`

## Paper-level fields

- `title`
- `short_name`
- `venue_year_status`
- `official_forum_url`
- `tags`
- `similarity_score` and a one-sentence explanation
- `why_it_matters`
- `review_scores`
- `decision_relevant_concerns`
- `author_response_status`: available, partially available, or unavailable
- `author_response_evidence`
- `effect_of_response`: score change, final justification, unresolved concern, or unknown
- `lessons_for_user`
- `per_review_notes`
- `meta_review_note`, when available

## Required distinctions in prose

Use visibly different labels for:

- **Reviewer concern** — what the reviewer explicitly challenged.
- **Author response** — what the authors explicitly answered or added.
- **Casebook implication** — the analysis applied to the user's project.
- **Missing record** — a public response was not available in the source consulted.

Never collapse these categories into a single narrative paragraph.

## Pre-review section

Write 6–10 questions as if reviewing the user's paper. Each entry must include:

- the likely reviewer question;
- why it threatens the claim;
- the concrete evidence needed before submission.

Prioritize construct validity, novelty against the nearest baseline, external validity, data integrity, judge reliability, statistical significance, computational cost, and claim scope.
