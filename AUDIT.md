# Final audit

Reviewed: 2026-09-20

Scope: `contracts/change_point_watch.py` at SHA-256 `0d0294f60c067929ba9f69c4f7a653adafa0bb3a6641a4f278ca5479b3731135`, its
tests and review documents, and the exact StudioNet deployment recorded in
`deployments/studionet.json`.

## Results

| Gate | Result |
| --- | --- |
| GenVM lint and semantic validation | PASS |
| Strict Pyright typecheck | PASS, zero diagnostics |
| Direct invariant and validator tests | PASS, 9 tests |
| Independent GLSim validators | PASS, exactly 5 validators |
| StudioNet deployment | PASS, FINALIZED |
| Real intelligent write | PASS, AGREE or MAJORITY_AGREE |
| Latest-final state readback | PASS |
| Deployed source byte equality | PASS |
| Deployed schema required-method read | PASS |
| Dependency and GenVM runner pins | PASS |
| Prompt-injection boundary and JSON normalization | PASS |
| Live-wallet handling | PASS, 2 fresh in-memory roles; keys never persisted |
| Cross-repository wallet reuse | NONE between the two 2026-09-20 deployments |
| Private key or mnemonic in repository | NONE |
| Workspace-wide originality scan | PASS, 161 contract sources scanned |
| GitHub destination (2026-08-28 publication update) | Private repository: Leokings/changepointwatch |

StudioNet contract: 0x166a33aaad7f14a4a741fA55f737ae4018483325

Deployment transaction: 0xb7c5107099c88fb58872e5aa315d3d66d1307746a628f41a783f4673f208509d

Intelligent transaction: 0x245b64d30062701befa4a63dc97d03106bdbe35bf75a582e5d3975fead5ab0d9

Observed live state: `{"baseline":[2,0],"downward_cusum":[0,0],"state":"MONITORING","upward_cusum":[0,0]}`

## Consensus review

Validators now normalize the leader payload through the same closed schema and
require exact agreement on every discrete signal band. This removes the prior
one-band leader-bias path that could accumulate into a false CUSUM change.
Dimension names are also unique case-insensitively.

## Review conclusion

No known source, build, test, consensus, wallet, secret, dependency, provenance,
or repository-hygiene blocker remains. Human program review can still apply its
own policy judgment; this audit does not promise acceptance.

Publication note: private GitHub evidence requires reviewer access. The
2026-09-20 StudioNet address contains the exact reviewed source. CI uses the
server's GET /health route for readiness; /api is a POST-only JSON-RPC route.
No live wallet key is stored in the repository or CI evidence.
