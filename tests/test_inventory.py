import pytest
from src.inventory.service import InventoryManager


def test_inventory_reserve_success():
    """Baseline test: Reserves stock when item has enough quantity."""
    mgr = InventoryManager()
    items = [{"id": 1, "stock": 10}, {"id": 2, "stock": 5}]
    res = mgr.reserve_stock(items, 4)
    assert res is True
    assert items[0]["stock"] == 6


def test_inventory_insufficient_stock_raises_index_error():
    """Defect Test: When no item satisfies quantity, loop len(items) + 1 causes IndexError."""
    mgr = InventoryManager()
    items = [{"id": 1, "stock": 2}, {"id": 2, "stock": 3}]
    # Should cleanly return False without crashing with IndexError: list index out of range
    res = mgr.reserve_stock(items, 100)
    assert res is False
