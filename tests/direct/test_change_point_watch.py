import json


DIMENSIONS = json.dumps(["Urgency", "Scope volatility"])
POLICY = "Map each public status snapshot to the two declared zero-to-four signal bands using explicit wording only."


def _open(contract, vm, owner, sensor, slack=1, threshold=2):
    vm.sender = owner
    return contract.open_watch("project-status", DIMENSIONS, slack, threshold, sensor, POLICY)


def _snapshot(contract, vm, sensor, watch_id, key, signals, text="The public status snapshot states ordinary urgency and stable scope conditions."):
    vm.sender = sensor
    vm.clear_mocks()
    vm.mock_llm(r".*Emit one closed semantic signal band for every monitored dimension.*", json.dumps({"signals": signals}))
    return contract.record_snapshot(watch_id, key, text)


def test_first_snapshot_establishes_baseline(contract, direct_vm, direct_alice, direct_bob):
    watch_id = _open(contract, direct_vm, direct_alice, direct_bob)
    _snapshot(contract, direct_vm, direct_bob, watch_id, "s0", [2, 2])
    watch = contract.get_watch(watch_id)
    assert watch["baseline"] == [2, 2]
    assert watch["state"] == "MONITORING"


def test_sustained_shift_crosses_cusum_threshold(contract, direct_vm, direct_alice, direct_bob):
    watch_id = _open(contract, direct_vm, direct_alice, direct_bob, 1, 2)
    _snapshot(contract, direct_vm, direct_bob, watch_id, "s0", [2, 2])
    _snapshot(contract, direct_vm, direct_bob, watch_id, "s1", [4, 2], "The public snapshot states extreme urgency while scope remains ordinary and stable.")
    _snapshot(contract, direct_vm, direct_bob, watch_id, "s2", [4, 2], "The next public snapshot again states extreme urgency while scope remains stable.")
    assert contract.changed_dimensions(watch_id) == [0]
    assert contract.get_watch(watch_id)["state"] == "CHANGE_DETECTED"


def test_owner_can_accept_detected_change_as_new_baseline(contract, direct_vm, direct_alice, direct_bob):
    watch_id = _open(contract, direct_vm, direct_alice, direct_bob, 0, 1)
    _snapshot(contract, direct_vm, direct_bob, watch_id, "s0", [2, 2])
    _snapshot(contract, direct_vm, direct_bob, watch_id, "s1", [3, 2], "The public snapshot states high urgency while scope remains ordinary and stable.")
    direct_vm.sender = direct_alice
    contract.accept_change_as_baseline(watch_id)
    assert contract.get_watch(watch_id)["baseline"] == [3, 2]
    assert contract.get_watch(watch_id)["state"] == "MONITORING"


def test_only_sensor_can_record(contract, direct_vm, direct_alice, direct_bob, direct_charlie):
    watch_id = _open(contract, direct_vm, direct_alice, direct_bob)
    direct_vm.sender = direct_charlie
    with direct_vm.expect_revert("only_sensor"):
        contract.record_snapshot(watch_id, "s0", "This otherwise valid status snapshot is submitted by an unauthorized wallet.")


def test_signal_band_is_bounded(contract, direct_vm, direct_alice, direct_bob):
    watch_id = _open(contract, direct_vm, direct_alice, direct_bob)
    direct_vm.sender = direct_bob
    direct_vm.mock_llm(r".*Emit one closed semantic signal band.*", json.dumps({"signals": [9, 2]}))
    with direct_vm.expect_revert("[LLM_ERROR] invalid_signal_band"):
        contract.record_snapshot(watch_id, "s0", "This valid-length public snapshot triggers a malformed model signal test.")


def test_validator_rejects_adjacent_signal_disagreement(contract, direct_vm, direct_alice, direct_bob):
    watch_id = _open(contract, direct_vm, direct_alice, direct_bob)
    _snapshot(contract, direct_vm, direct_bob, watch_id, "s0", [2, 2])
    assert direct_vm.run_validator() is True
    direct_vm.clear_mocks()
    direct_vm.mock_llm(
        r".*Emit one closed semantic signal band for every monitored dimension.*",
        json.dumps({"signals": [3, 2]}),
    )
    assert direct_vm.run_validator() is False


def test_validator_rejects_extra_leader_fields(contract, direct_vm, direct_alice, direct_bob):
    watch_id = _open(contract, direct_vm, direct_alice, direct_bob)
    _snapshot(contract, direct_vm, direct_bob, watch_id, "s0", [2, 2])
    assert direct_vm.run_validator(leader_result={"signals": [2, 2], "extra": True}) is False


def test_dimension_names_must_be_unique_case_insensitively(contract, direct_vm, direct_alice, direct_bob):
    direct_vm.sender = direct_alice
    with direct_vm.expect_revert("duplicate_dimension"):
        contract.open_watch(
            "duplicate-dimensions",
            json.dumps(["Urgency", "urgency"]),
            1,
            2,
            direct_bob,
            POLICY,
        )


def test_zero_address_cannot_be_the_sensor(contract, direct_vm, direct_alice):
    direct_vm.sender = direct_alice
    with direct_vm.expect_revert("invalid_sensor"):
        contract.open_watch(
            "zero-sensor",
            DIMENSIONS,
            1,
            2,
            "0x" + "0" * 40,
            POLICY,
        )
