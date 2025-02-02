class Node:
    """A Node in the Doubly Linked List."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCacheDLL:
    """LRU Cache using Doubly Linked List and HashMap."""
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Stores key -> Node mapping
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Removes a node from the list."""
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _add_to_front(self, node):
        """Adds a node right after the head (most recently used)."""
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node

    def get(self, key: int) -> int:
        """Returns value if key exists, else -1."""
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int):
        """Inserts/Updates key-value, removing LRU if full."""
        if key in self.cache:
            self._remove(self.cache[key])
        elif len(self.cache) >= self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        new_node = Node(key, value)
        self._add_to_front(new_node)
        self.cache[key] = new_node
