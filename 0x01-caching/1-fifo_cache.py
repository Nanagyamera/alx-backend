#!/usr/bin/python3
"""
Task 1
"""


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and implements a caching system with FIFO eviction policy
    """

    def __init__(self):
        """ Initialize the FIFOCache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict()
            self.cache_data[key] = item
            self.queue.append(key)

    def evict(self):
        """ Evict the first item in the cache (FIFO eviction)
        """
        if self.queue:
            key_to_evict = self.queue.pop(0)
            del self.cache_data[key_to_evict]
            print("DISCARD:", key_to_evict)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
