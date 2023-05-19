#!/usr/bin/env python3
"""
    FIFOCache is a class that inherits from BaseCaching and is a caching syste
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """This function represents an object that allows storing and
    retrieving items from a dictionary with a FIFO
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """This function initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        The put function get  dictionary self.cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """
        The get function must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
