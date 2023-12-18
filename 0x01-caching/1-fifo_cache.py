#!/usr/bin/python3
"""class FIFOCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A subclass FIFOCache that inherits from BaseCaching"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Assigns the items to the dictionary"""

        if item is not None and key is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = sorted(self.cache_data)[0]
            self.cache_data.pop(first_key)
            print('DISCARD: {}'.format(first_key))

    def get(self, key):
        """Returns the value that is linked to the key"""

        if key is None and key in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
