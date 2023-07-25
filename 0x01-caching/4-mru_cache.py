#!/usr/bin/python3
"""
Task4
"""


class MRUCache(BaseCaching):
    """
    MRUCache inherits from BaseCaching and implements a caching system with MRU eviction policy
    """

    def __init__(self):
        """
        Initialize the MRUCache
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
        Evict the most recently used item from the cache (MRU eviction)
        """
        if self.queue:
            key_to_evict = self.queue.pop()
            del self.cache_data[key_to_evict]
            print("DISCARD:", key_to_evict)

    def get(self, key):
        """
        Get an item by key (update the queue for MRU)
        """
        if key is not None:
            value = self.cache_data.get(key)
            if value is not None:
                self.queue.remove(key)
                self.queue.append(key)
            return value
        return None
