#!/usr/bin/python3
"""
LIFO caching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching and implements a caching
    system with LIFO eviction policy
    """

    def __init__(self):
        """
        Initialize the LIFOCache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict()
            self.cache_data[key] = item
            self.queue.append(key)

    def evict(self):
        """
        Evict the last item in the cache (LIFO eviction)
        """
        if self.queue:
            key_to_evict = self.queue.pop()
            del self.cache_data[key_to_evict]
            print("DISCARD:", key_to_evict)

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
