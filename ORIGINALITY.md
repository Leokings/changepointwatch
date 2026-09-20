# Originality audit

The original mechanism source was compared against 161 GenLayer contract
sources in the workspace. All twenty new target contracts were excluded from
the pre-existing comparison pool. The 2026-09-20 hardening changed only the
consensus boundary and duplicate-dimension validation; it did not introduce a
new mechanism or copy another implementation.

Nearest pre-existing source: `rulebender\contracts\policy_amendment_chain.py`

Combined structural score: `0.202996`

Token score: `0.325688`

AST score: `0.11472`

Nearest contract in this new set: `coveragemosaic\contracts\coverage_mosaic.py` with combined
score `0.379871`. That score reflects shared safe GenLayer
boilerplate. The mechanisms differ materially:

- This repository: Consensus emits a closed signal vector for each snapshot; deterministic per-dimension CUSUM detects sustained change rather than a one-off difference.
- Other repository: Consensus verifies which claimed cells are supported by one observation; deterministic bitmap union and gap calculation control sealing.

The two do not share the same semantic input, deterministic algorithm, storage
record, state lifecycle, or decision views. Exact source SHA-256 values are also
unique across all twenty repositories. The complete machine-readable reports are
`review-tools/twenty-originality-audit.json` and
`review-tools/twenty-pairwise-audit.json` at the workspace level.

Similarity scoring is a review aid, not a guarantee of a human review outcome.

## Accepted/pending Portal comparison — 2026-09-20

The title and mechanism were checked against the 26 accepted and two pending
Portal submissions. No submission uses longitudinal semantic signals with a
deterministic two-sided CUSUM. The closest concepts remain materially distinct:

- `Rubric Calibration Lock` reaches a one-time calibration decision; it does
  not maintain a signal time series or accumulate positive and negative drift.
- `Dependency Lifecycle Oracle` assesses external dependency lifecycle data;
  it does not monitor caller snapshots against a baseline.
- `Agent Output Grounding Verifier` checks claims against evidence; it does not
  perform change-point detection.

A workspace search outside this repository found no other Python contract using
`CUSUM`, `change_dimensions`, `change_point`, or `change point`.
