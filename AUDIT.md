# Final audit

Reviewed: 2026-08-25

Scope: `contracts/change_point_watch.py` at SHA-256 `3fe5391818f88794f49b8332937c11be0ef02117ffaae4ca9782d882690d8fb8`, its
tests and review documents, and the exact StudioNet deployment recorded in
`deployments/studionet.json`.

## Results

| Gate | Result |
| --- | --- |
| GenVM lint and semantic validation | PASS |
| Strict Pyright typecheck | PASS, zero diagnostics |
| Direct invariant tests | PASS, 5 tests |
| Independent GLSim validators | PASS, exactly 5 validators |
| StudioNet deployment | PASS, FINALIZED |
| Real intelligent write | PASS, AGREE or MAJORITY_AGREE |
| Latest-final state readback | PASS |
| Deployed source byte equality | PASS |
| Deployed schema required-method read | PASS |
| Dependency and GenVM runner pins | PASS |
| Prompt-injection boundary and JSON normalization | PASS |
| External wallet isolation | PASS, 5 unique roles for this repository |
| Cross-repository wallet reuse | NONE across 100 roles |
| Private key or mnemonic in repository | NONE |
| Workspace-wide originality scan | PASS, 161 contract sources scanned |
| GitHub destination (2026-08-28 publication update) | Private repository: Leokings/changepointwatch |

StudioNet contract: 0xB89CfedB9495a44f0E2a35EDfdCA77CE0Db495e0

Deployment transaction: 0x4fa5073f936228b7240ed68e13720559c1a3c4b89e971d98461c39b4f6b8743a

Intelligent transaction: 0x4ece532d5de99ad77071e420704f152809bfba22d771577a964a7ed552f2c0f8

Observed live state: `{"baseline":[2,1],"downward_cusum":[0,0],"state":"MONITORING","upward_cusum":[0,0]}`

## Consensus review

Validators accept adjacent semantic bands within one step; deterministic CUSUM state remains bounded and explicit.

## Review conclusion

No known source, build, test, consensus, wallet, secret, dependency, provenance,
or repository-hygiene blocker remains. Human program review can still apply its
own policy judgment; this audit does not promise acceptance.

Publication note: private GitHub evidence requires reviewer access. The original
StudioNet source and wallets are unchanged. CI uses the server's GET /health route
for readiness; /api is a POST-only JSON-RPC route. No live wallet keys are used by CI.
