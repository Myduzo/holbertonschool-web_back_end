#!/usr/bin/env python3
"""0. Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""
    def put(self, key, item):
        """assign key: item to the dict"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value of the key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
