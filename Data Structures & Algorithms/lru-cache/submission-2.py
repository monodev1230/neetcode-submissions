class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.lru = ListNode(0, 0)
        self.mru = ListNode(0, 0)
        self.lru.next, self.mru.prev = self.mru, self.lru

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.cache[node.key]
    
    def insert(self, node):
        self.mru.prev.next = node
        node.prev = self.mru.prev
        node.next = self.mru
        self.mru.prev = node
        self.cache[node.key] = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cap += 1
        if self.cap == 0:
            self.remove(self.lru.next)
            self.cap += 1
        newNode = ListNode(key, value)
        self.insert(newNode)
        self.cap -= 1

