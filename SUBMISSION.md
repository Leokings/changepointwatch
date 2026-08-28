Project name: ChangePointWatch

Category: Intelligent Contracts

Batch: B

One-line description: Semantic cumulative-sum change detection.

What it does: Consensus emits a closed signal vector for each snapshot; deterministic per-dimension CUSUM detects sustained change rather than a one-off difference.

Why GenLayer: GenLayer consensus performs the bounded semantic step, then deterministic contract code executes and stores the mechanism-specific result.

Reusable: Yes. One deployment supports many independently keyed records and callers; the live fixture is only an example.

Repository: https://github.com/Leokings/changepointwatch (private; reviewers require read access).

Contract source: contracts/change_point_watch.py

Source SHA-256: 3fe5391818f88794f49b8332937c11be0ef02117ffaae4ca9782d882690d8fb8

StudioNet contract: https://explorer-studio.genlayer.com/address/0xB89CfedB9495a44f0E2a35EDfdCA77CE0Db495e0

Deployment transaction: https://explorer-studio.genlayer.com/tx/0x4fa5073f936228b7240ed68e13720559c1a3c4b89e971d98461c39b4f6b8743a

Intelligent transaction: https://explorer-studio.genlayer.com/tx/0x4ece532d5de99ad77071e420704f152809bfba22d771577a964a7ed552f2c0f8

Verification: GenVM lint PASS; strict typecheck PASS; 5 direct tests PASS; five-validator GLSim PASS; finalized StudioNet intelligent write and latest-final readback PASS; exact deployed-source and schema verification PASS.

Originality: Compared with 161 workspace contract sources. Nearest pre-existing structural score is 0.202996; mechanism and source hash are distinct.

Data boundary: Caller-supplied public data only. No external source fetching, funds, identity attestation, legal effect, or private-data guarantee.

Plain-text portal fields: SUBMISSION.txt. Notes / Description is within the 1,000-character form limit.
