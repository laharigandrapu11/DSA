# Last updated: 7/27/2025, 4:54:50 PM
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []  # Most Recently Used at front (index 0)

    def get(self, key: int) -> int:
        if key in self.cache:
            self.order.remove(key)
            self.order.insert(0, key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
            self.order.insert(0, key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                lru = self.order.pop()     # Least Recently Used
                del self.cache[lru]
            self.order.insert(0, key)      # Add new key as MRU
            self.cache[key] = value
