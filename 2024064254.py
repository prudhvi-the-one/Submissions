class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key not in self.cache:
            return -1

        self.order.remove(key)
        self.order.append(key)

        return self.cache[key]

    def put(self, key, value):

        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)

        else:
            if len(self.cache) == self.capacity:
                lru = self.order.pop(0)
                del self.cache[lru]

            self.cache[key] = value
            self.order.append(key)


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)

print(cache.get(1))

cache.put(3, 3)

print(cache.get(2))

cache.put(4, 4)

print(cache.get(1))
print(cache.get(3))
print(cache.get(4))









