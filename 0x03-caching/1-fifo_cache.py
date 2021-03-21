#!/usr/bin/env python3
"""1. FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class"""
    def __init__(self):
        """Initialisation of variables"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """PUT method with FIFO queue"""
        if key or item:
            if key in self.cache_data:
                self.cache_data[key] = item

            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    print('DISCARD: ' + self.queue[0])
                    del self.cache_data[self.queue[0]]
                    del self.queue[0]
                self.cache_data[key] = item
                self.queue.append(key)

    def get(self, key):
        """GET method"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
