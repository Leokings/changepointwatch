import json
from pathlib import Path
from gltest import get_contract_factory, get_validator_factory
from gltest.accounts import create_accounts
from gltest.assertions import tx_execution_succeeded
from gltest.types import TransactionStatus
from gltest.utils import extract_contract_address


def _ok(receipt):
    assert tx_execution_succeeded(receipt), json.dumps(receipt, default=str)


def _context(signals):
    validators = get_validator_factory().batch_create_mock_validators(5, mock_llm_response={"nondet_exec_prompt": {"Emit one closed semantic signal band for every monitored dimension": json.dumps({"signals": signals})}})
    return {"validators": [v.to_dict() for v in validators], "genvm_datetime": "2026-08-25T12:00:00Z"}


def test_five_validator_change_point_flow():
    owner, sensor = create_accounts(2)
    factory = get_contract_factory(contract_file_path=Path(__file__).resolve().parents[2] / "contracts" / "change_point_watch.py")
    receipt = factory.deploy_contract_tx(args=[], account=owner, wait_transaction_status=TransactionStatus.FINALIZED)
    _ok(receipt)
    address = extract_contract_address(receipt)
    admin = factory.build_contract(address, account=owner)
    recorder = factory.build_contract(address, account=sensor)
    watch_id = f"{str(owner.address).lower()}:PROJECT-STATUS"
    _ok(admin.open_watch(args=["project-status", json.dumps(["Urgency", "Scope volatility"]), 0, 1, sensor.address, "Map explicit snapshot wording to the declared zero-to-four bands." ]).transact(wait_transaction_status=TransactionStatus.FINALIZED))
    _ok(recorder.record_snapshot(args=[watch_id, "s0", "The public status snapshot states ordinary urgency and stable scope conditions."]).transact(transaction_context=_context([2, 2]), wait_transaction_status=TransactionStatus.FINALIZED))
    _ok(recorder.record_snapshot(args=[watch_id, "s1", "The public status snapshot states high urgency and stable scope conditions."]).transact(transaction_context=_context([3, 2]), wait_transaction_status=TransactionStatus.FINALIZED))
    assert recorder.changed_dimensions(args=[watch_id]).call() == [0]
