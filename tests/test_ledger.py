import pytest
import threading
from src.payments.ledger import PaymentLedger


def test_ledger_single_transfer():
    """Baseline test: Single sequential transfer succeeds."""
    ledger = PaymentLedger({"alice": 100.0, "bob": 50.0})
    success = ledger.transfer_funds("alice", "bob", 30.0)
    assert success is True
    assert ledger.balances["alice"] == 70.0
    assert ledger.balances["bob"] == 80.0


def test_ledger_concurrent_double_spend():
    """Defect Test: Two concurrent transfers of 80 from an account with only 100 should not both succeed."""
    ledger = PaymentLedger({"alice": 100.0, "bob": 0.0})
    results = []

    def attempt_transfer():
        res = ledger.transfer_funds("alice", "bob", 80.0)
        results.append(res)

    t1 = threading.Thread(target=attempt_transfer)
    t2 = threading.Thread(target=attempt_transfer)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # Exactly one transfer should succeed, total Alice balance cannot be negative
    assert ledger.balances["alice"] >= 0.0, f"Account balance went negative: {ledger.balances['alice']}"
    assert results.count(True) == 1, "Race condition allowed both concurrent transfers to succeed!"
