class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.right = Node()
        self.left = Node()
        self.right.prev, self.left.next = self.left, self.right

        self.capacity = capacity
        self.map = {}

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node):
        prev, tail = self.right.prev, self.right
        node.prev, node.next = prev, tail
        tail.prev = prev.next = node

    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.insert(self.map[key])
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        self.map[key] = Node(key, value)
        self.insert(self.map[key])
        
        if len(self.map) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.map[lru.key]
        
        
