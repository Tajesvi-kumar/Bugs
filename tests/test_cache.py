import pytest
from src.cache.lru import LRUCache


def test_cache_normal_eviction():
    """Baseline test: Cache evicts after size grows."""
    cache = LRUCache(capacity=2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    cache.put("d", 4)
    # Cache should not grow without bound
    assert len(cache.cache) <= 3


def test_cache_strict_capacity_invariable():
    """Defect Test: A cache with capacity=2 should NEVER hold 3 items at once."""
    cache = LRUCache(capacity=2)
    cache.put("k1", "v1")
    cache.put("k2", "v2")
    cache.put("k3", "v3")

    # Due to `len > capacity + 1` bug, len(cache) is 3 instead of 2!
    assert len(cache.cache) == 2, f"LRU cache exceeded capacity limit! Expected 2, got {len(cache.cache)}"
