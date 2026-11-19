"""Pagination helper module containing offset calculation defect."""

from typing import List, Any


def get_page_slice(items: List[Any], page: int, page_size: int) -> List[Any]:
    """Calculates slice of items for given 1-indexed page.

    DEFECT: `offset = page * page_size` omits `page - 1` shift, dropping the first page entirely.
    """
    # Defect: 1-based pagination missing offset subtraction
    offset = page * page_size
    return items[offset:offset + page_size]
