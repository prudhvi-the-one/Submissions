class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict1 = {}

    def get(self, key: int) -> int:
        if key in self.dict1:
            val = self.dict1[key]
            del self.dict1[key]
            self.dict1[key] = val
            return self.dict1[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.dict1)<=self.capacity:
            self.dict1[key] = value
        else:
            del self.dict1[key]
            self.dict1[key] = value

new = LRUCache(2)

print(new.get(1))
new.put(1,3)
print(new.get(1))
print(new.get(2))
