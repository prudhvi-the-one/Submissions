from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)

        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value

    def display(self):
        print("Current Cache:")
        for key, value in self.cache.items():
            print(f"{key} -> {value}")
        print()



cache = LRUCache(2)

print("Adding (1,1)")
cache.put(1, 1)
cache.display()

print("Adding (2,2)")
cache.put(2, 2)
cache.display()

print("Value of key 1:", cache.get(1))
cache.display()

print("Adding (3,3)")
cache.put(3, 3)
cache.display()

print("Value of key 2:", cache.get(2))

print("Adding (4,4)")
cache.put(4, 4)
cache.display()

print("Value of key 1:", cache.get(1))
print("Value of key 3:", cache.get(3))
print("Value of key 4:", cache.get(4))
