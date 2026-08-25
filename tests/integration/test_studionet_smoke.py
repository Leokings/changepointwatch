import json
import os
from pathlib import Path

import pytest
from gltest import get_contract_factory
from gltest.types import TransactionHashVariant, TransactionStatus
from gltest.utils import extract_contract_address

from tests.studionet_support import emit_record, ok, source_schema_proof, wallet_accounts


pytestmark = [
    pytest.mark.integration,
    pytest.mark.skipif(os.environ.get("RUN_STUDIONET") != "1", reason="opt-in live StudioNet test"),
]


def test_studionet_semantic_change_point_watch():
    accounts = wallet_accounts("changepointwatch", 2)
    owner, sensor = accounts[:2]
    source = Path(__file__).resolve().parents[2] / "contracts" / "change_point_watch.py"
    factory = get_contract_factory(contract_file_path=source)
    deployed = ok(factory.deploy_contract_tx(args=[], account=owner, wait_transaction_status=TransactionStatus.FINALIZED))
    address = extract_contract_address(deployed)
    admin = factory.build_contract(address, account=owner)
    recorder = factory.build_contract(address, account=sensor)
    watch_id = f"{str(owner.address).lower()}:PROJECT-STATUS"
    setup = ok(admin.open_watch(args=["project-status", json.dumps(["Urgency", "Scope volatility"]), 0, 2, sensor.address, "Map explicit snapshot wording to the declared zero-to-four signal bands." ]).transact(wait_transaction_status=TransactionStatus.FINALIZED))
    intelligent = ok(recorder.record_snapshot(args=[watch_id, "baseline", "The public status snapshot states ordinary urgency and stable scope conditions." ]).transact(wait_transaction_status=TransactionStatus.FINALIZED))
    state = admin.get_watch(args=[watch_id]).call(transaction_hash_variant=TransactionHashVariant.LATEST_FINAL)
    assert state["schema"] == "changepointwatch/watch/v1" and state["state"] == "MONITORING" and len(state["baseline"]) == 2
    proof = source_schema_proof(address, source, {"record_snapshot", "accept_change_as_baseline", "changed_dimensions"})
    emit_record("changepointwatch", "B", address, deployed, [setup], intelligent, accounts, proof, {"state": state["state"], "baseline": state["baseline"], "upward_cusum": state["upward_cusum"], "downward_cusum": state["downward_cusum"]})
