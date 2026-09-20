# ChangePointWatch

Semantic cumulative-sum change detection.

Batch: B

## Why it is GenLayer-native

Consensus emits a closed signal vector for each snapshot; deterministic per-dimension CUSUM detects sustained change rather than a one-off difference.

The LLM handles only the bounded semantic step. Deterministic contract code owns
the reusable algorithm, state transitions, access control, tie-breaking, and
views. One deployment supports many caller-keyed records; it is not tied to the
StudioNet fixture or one organization.

## Public interface

Write methods: `open_watch`, `record_snapshot`, `accept_change_as_baseline`

View methods: `get_watch`, `get_snapshot`, `changed_dimensions`

## Verification

```text
pip install -r requirements.txt
genvm-lint check contracts/change_point_watch.py
genvm-lint typecheck contracts/change_point_watch.py --strict
pytest tests/direct -q
python tests/run_glsim.py --port 4000 --validators 5
gltest tests/integration -q --network localnet
```

The live smoke test is opt-in and creates fresh disposable wallets in memory by
default; an external repository-specific wallet bundle is optional. It waits
for finalized receipts, reads `LATEST_FINAL`, retrieves deployed source and
schema from StudioNet, and fails unless the source bytes exactly match this
repository. Private keys are never printed or persisted by the default path.

StudioNet contract: https://explorer-studio.genlayer.com/address/0x166a33aaad7f14a4a741fA55f737ae4018483325

See `AUDIT.md`, `ORIGINALITY.md`, `SOURCE_POLICY.md`, `SECURITY.md`,
`SUBMISSION.md`, and `deployments/studionet.json` for the final evidence.

## Boundary

The contract moves no funds and does not establish identity, ownership,
professional authority, source authenticity, physical truth, or legal effect.
All caller inputs and calldata are public. Off-chain clients own authentication,
privacy, source curation, indexing, and the decision to rely on a result.
