#!/usr/bin/python3
"""
Task 5
"""
from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching and implements a
    caching system with LFU eviction policy
    """

    def __init__(self):
        """
        Initialize the LFUCache
        """
        super().__init__()
        self.frequency_counter = defaultdict(int)
        self.min_frequency = 0

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict()
            self.cache_data[key] = item
            self.frequency_counter[key] += 1
            self.min_frequency = 1

    def evict(self):
        """
        Evict the least frequency used item from the cache (LFU eviction)
        """
        items_to_discard = [key for key, freq in self.frequency_counter.items()
                            if freq == self.min_frequency]
        key_to_evict = self.lru_evict(items_to_discard)
        del self.cache_data[key_to_evict]
        del self.frequency_counter[key_to_evict]
        print("DISCARD:", key_to_evict)

    def lru_evict(self, items):
        """
        Evict the least recently used item from the given items (LRU eviction)
        """
        if not self.queue:
            return None

        for key in self.queue:
            if key in items:
                return key

    def get(self, key):
        """
        Get an item by key (update the frequency counter)
        """
        if key is not None:
            value = self.cache_data.get(key)
            if value is not None:
                self.frequency_counter[key] += 1
                if self.frequency_counter[key] > self.min_frequency:
                    self.min_frequency = self.frequency_counter[key]
            return value
        return None
