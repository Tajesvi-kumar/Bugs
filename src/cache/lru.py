"""LRU Cache module containing capacity boundary overrun defect."""

from collections import OrderedDict
from typing import Any, Optional


class LRUCache:
    """Least Recently Used (LRU) key-value cache."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: OrderedDict = OrderedDict()

    def get(self, key: str) -> Optional[Any]:
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: str, value: Any) -> None:
        """Inserts key and evicts oldest element if capacity exceeded.

        DEFECT: Eviction check uses `> self.capacity + 1` instead of `> self.capacity`,
        allowing the cache to store up to capacity + 1 items before evicting.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        # Defect: Off-by-one boundary allows memory leak
        if len(self.cache) > self.capacity + 1:
            self.cache.popitem(last=False)
