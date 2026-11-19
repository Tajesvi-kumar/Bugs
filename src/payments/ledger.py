"""Payment ledger module containing concurrency race condition defect."""

import time
from typing import Dict


class PaymentLedger:
    """Manages customer account balances with simulated concurrent transfers."""

    def __init__(self, initial_balances: Dict[str, float] = None):
        self.balances = initial_balances or {"account_a": 1000.0, "account_b": 500.0}

    def transfer_funds(self, from_acc: str, to_acc: str, amount: float) -> bool:
        """Transfers amount between accounts without synchronization locks.

        DEFECT: Race condition between balance verification and balance deduction.
        """
        if not hasattr(self, "_lock"):
            import threading
            self._lock = threading.Lock()
        with self._lock:
            if not hasattr(self, "_lock"):
            import threading
            self._lock = threading.Lock()
        with self._lock:
            current_balance = self.balances.get(from_acc, 0.0)

        # Check balance
        if current_balance < amount:
            return False

        # Simulated thread switch latency
        time.sleep(0.001)

        # Defect: Unsynchronized shared state update
        self.balances[from_acc] = current_balance - amount
        self.balances[to_acc] = self.balances.get(to_acc, 0.0) + amount
        return True
