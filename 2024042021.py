class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.p = None
        self.n = None


class LRUCache:

    def __init__(self, cap):
        self.cap = cap
        self.store = {}
        self.h = Node(0, 0)
        self.t = Node(0, 0)
        self.h.n = self.t
        self.t.p = self.h

    def cut(self, node):
        node.p.n = node.n
        node.n.p = node.p

    def add(self, node):
        before = self.t.p
        before.n = node
        node.p = before
        node.n = self.t
        self.t.p = node

    def get(self, key):
        if key not in self.store:
            return -1
        nd = self.store[key]
        self.cut(nd)
        self.add(nd)
        return nd.v

    def put(self, key, val):
        if key in self.store:
            self.cut(self.store[key])
            del self.store[key]
        nd = Node(key, val)
        self.store[key] = nd
        self.add(nd)
        if len(self.store) > self.cap:
            old = self.h.n
            self.cut(old)
            del self.store[old.k]


cap = int(input("Enter Capacity: "))
cache = LRUCache(cap)

ops = int(input("Enter Number of Operations: "))

print("\nCommands:")
print("put key value")
print("get key")
print("display")
print("exit")

for _ in range(ops):

    cmd = input().split()

    if cmd[0] == "put":
        k = int(cmd[1])
        v = int(cmd[2])
        cache.put(k, v)
        print("Inserted")

    elif cmd[0] == "get":
        k = int(cmd[1])
        print(cache.get(k))

    elif cmd[0] == "display":
        cur = cache.h.n
        while cur != cache.t:
            print(f"{cur.k}:{cur.v}", end=" ")
            cur = cur.n
        print()

    elif cmd[0] == "exit":
        break