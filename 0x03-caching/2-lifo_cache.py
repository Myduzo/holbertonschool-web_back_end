#!/usr/bin/env python3
"""2. LIFO Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class"""
    def __init__(self):
        """Initialisation of variables"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """PUT method with LIFO queue"""
        if key or item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.queue.remove(key)
                self.queue[:0] = [key]

            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    print('DISCARD: ' + self.queue[0])
                    del self.cache_data[self.queue[0]]
                    del self.queue[0]
                self.queue[:0] = [key]
                self.cache_data[key] = item

    def get(self, key):
        """GET method"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
