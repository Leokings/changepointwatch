# Intelligent-contract submission

## Title

ChangePointWatch — Semantic CUSUM Change Detection

## Description

ChangePointWatch is a reusable GenLayer intelligent contract for detecting
sustained semantic change in public, caller-supplied snapshots. For each
snapshot, GenLayer validators independently produce the same bounded 0–4 signal
vector under a caller-defined policy. Deterministic contract code then applies
two-sided per-dimension CUSUM, records the audit trail, identifies changed
dimensions, and lets the watch owner explicitly accept a detected change as the
new baseline. One deployment supports many owner-keyed watches and separate
sensor wallets. The reviewed version requires an exact closed leader schema and
exact validator agreement, preventing a one-band leader bias from accumulating
into a false change. It also rejects an unusable zero-address sensor. GenVM lint
and strict type checking pass, all 9 direct tests pass, the five-validator GLSim
flow passes, and the exact source was redeployed and exercised successfully on
StudioNet on 2026-09-20.

## Evidence

- Contract: https://explorer-studio.genlayer.com/address/0x166a33aaad7f14a4a741fA55f737ae4018483325
- Deployment: https://explorer-studio.genlayer.com/tx/0xb7c5107099c88fb58872e5aa315d3d66d1307746a628f41a783f4673f208509d
- Intelligent write: https://explorer-studio.genlayer.com/tx/0x245b64d30062701befa4a63dc97d03106bdbe35bf75a582e5d3975fead5ab0d9
- Exact-source proof: https://github.com/Leokings/changepointwatch/blob/main/deployments/studionet.json

## GitHub repository

https://github.com/Leokings/changepointwatch
