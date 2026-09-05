class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.put_mru(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.put_mru(node)
            return

        node = Node(key, value)
        self.cache[key] = node

        if len(self.cache) == 1:
            self.head = node
            self.tail = node
        else:
            self.put_mru(node)

        if len(self.cache) > self.capacity:
            self.remove_lru()

    def put_mru(self, node: Node) -> None:
        if node is self.head:
            return

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node is self.tail:
            self.tail = node.prev

        node.prev = None
        node.next = self.head

        if self.head:
            self.head.prev = node

        self.head = node

        if self.tail is None:
            self.tail = node

    def remove_lru(self) -> None:
        if self.tail is None:
            return

        lru = self.tail
        del self.cache[lru.key]
        self.tail = lru.prev

        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        lru.prev = None
        lru.next = None