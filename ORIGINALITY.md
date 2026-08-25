# Originality audit

The final source was compared against 161 GenLayer
contract sources in the workspace. All twenty new target contracts were excluded
from the pre-existing comparison pool.

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
