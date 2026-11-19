import pytest
from src.billing.discount import calculate_tiered_discount


def test_billing_non_vip_zero_discount():
    """Baseline test: Non-VIP receives 0% discount."""
    assert calculate_tiered_discount(250.0, is_vip=False) == 0.0


def test_billing_vip_under_500():
    """Baseline test: VIP under 500 receives 10% discount."""
    assert calculate_tiered_discount(300.0, is_vip=True) == 0.10


def test_billing_vip_exact_threshold():
    """Defect Test: VIP order of exactly $500 should receive tier 1 (10%) discount, but buggy code drops to 0.0."""
    discount = calculate_tiered_discount(500.0, is_vip=True)
    assert discount == 0.10, f"Expected 0.10 discount for $500 threshold, got {discount}"
