#!/usr/bin/env python3
"""
LIFOCache is a class that inherits from BaseCaching and is a caching system:
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
        """This class represents an object that allows storing and
    retrieving items from a dictionary.
    """
    def __init__(self):
        """
        Initializes the class
        must use self.cache_data - dictionary from the parent class BaseCaching
            You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        The put function must assign to the dictionary self.cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        The get function must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
