#!/usr/bin/python3
"""Create class LIFOCache that inherits from BaseCaching.Its caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A subclass of parent class Bacaching"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Assigns the items to the dictionary"""

        if item is not None and key is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print('DISCARD: {}'.format(self.last_item))
            self.cache_data.pop(self.last_item)
        self.last_item = key

    def get(self, key):
        """Returns the value that is linked to the key"""

        if key is None and key in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
