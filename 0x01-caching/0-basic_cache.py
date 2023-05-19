#!/usr/bin/env python3
"""
 class BasicCache is a class that inherits from BaseCaching and is a caching system

"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """This function represents an object that allows storing and
    retrieving items from a dictionary.
    """
    def put(self, key, item):
        """
        The put function must assign to the dictionary self.cache_data the item value for the key key.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        The get function must return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)
