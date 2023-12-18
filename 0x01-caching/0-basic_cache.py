#!/usr/bin/python3
"""Caching system that Create class BasicCache inherited from BaseCaching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A subclass from parent class BaseCaching"""

    def put(self, key, item):
        """Assigns the items to the dictionary"""

        if item is not None and key is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value that is linked to the key"""

        if key is None and key in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
