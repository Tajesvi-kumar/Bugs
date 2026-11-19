"""Inventory Service module containing loop boundary off-by-one defect."""

from typing import List, Dict, Any


class InventoryManager:
    """Manages product stock reservations."""

    def reserve_stock(self, items: List[Dict[str, Any]], quantity: int) -> bool:
        """Finds first warehouse item with sufficient inventory and reserves stock.

        DEFECT: Range uses `len(items) + 1`, causing IndexError when all items have insufficient stock.
        """
        # Defect: Off-by-one boundary overshoot
        for i in range(len(items) + 1):
            if items[i]["stock"] >= quantity:
                items[i]["stock"] -= quantity
                return True
        return False
