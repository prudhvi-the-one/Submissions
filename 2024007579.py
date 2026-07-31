class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.nxt = None

class LRUCache:
    def __init__(self, cap: int):
        self.cap = cap
        self.m = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def _rem(self, node):
        p, n = node.prev, node.nxt
        p.nxt = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.nxt = node
        node.prev = p
        node.nxt = self.tail
        self.tail.prev = node

    def get(self, k: int) -> int:
        if k not in self.m:
            return -1
        node = self.m[k]
        self._rem(node)
        self._add(node)
        return node.v

    def put(self, k: int, v: int) -> None:
        if k in self.m:
            self._rem(self.m[k])
        node = Node(k, v)
        self._add(node)
        self.m[k] = node
        if len(self.m) > self.cap:
            lru = self.head.nxt
            self._rem(lru)
            del self.m[lru.k]

cache = LRUCache(2)
print(cache.get(3))
