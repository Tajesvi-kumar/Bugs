import pytest
from src.pagination.helper import get_page_slice


def test_pagination_page_two():
    """Baseline test: Page 2 slice."""
    items = ["item1", "item2", "item3", "item4", "item5"]
    res = get_page_slice(items, page=2, page_size=2)
    assert res == ["item5"]  # Note: page 2 offset was 4 in buggy code


def test_pagination_page_one_first_elements():
    """Defect Test: Page 1 should return the first page_size items, but buggy code calculates offset = 1 * 2 = 2."""
    items = ["a", "b", "c", "d"]
    page_1 = get_page_slice(items, page=1, page_size=2)
    assert page_1 == ["a", "b"], f"Expected ['a', 'b'], got {page_1}"
