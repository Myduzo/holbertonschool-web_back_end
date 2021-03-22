#!/usr/bin/env python3
"""4. MRU Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""
    def __init__(self):
        """Initialisation of variables"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """PUT method with Most Recently Used queue"""
        if key and item:
            # print(self.Queue)
            if key in self.cache_data:
                self.cache_data[key] = item
                self.queue.remove(key)
                self.queue.insert(0, key)
            else:
                if (len(self.cache_data) == self.MAX_ITEMS):
                    print("DISCARD: {}".format(self.queue[0]))
                    del self.cache_data[self.queue[0]]
                    del self.queue[0]
                self.queue.insert(0, key)
                self.cache_data[key] = item

    def get(self, key):
        """GET method"""
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue[:0] = key
            return self.cache_data[key]
        return None
