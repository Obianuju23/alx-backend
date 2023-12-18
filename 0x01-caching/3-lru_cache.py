#!/usr/bin/python3
"""class LRUCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A subclass of parent class Bacaching"""
    def __init__(self):
        """initialises the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """assigns value based on lifo to the dictionary"""
        if key is not None and item is not None:
            if len(self.cache_data) >= super().MAX_ITEMS:
                lru_key = self.order.pop(0)
                print("DISCARD: {}".format(lru_key))
                del self.cache_data[lru_key]

            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)

    def get(self, key):
        """returns the value of the key"""
        if key is not None:
            if key in self.cache_data:
                self.order.remove(key)
                self.order.append(key)
                return self.cache_data[key]
        return None
