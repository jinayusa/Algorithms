from collections import OrderedDict

class LRUCache:
    """Least Recently Used (LRU) Cache using OrderedDict."""
    
    def __init__(self, capacity: int):
        """
        Initializes the LRU Cache with a given capacity.
        Time Complexity: O(1) (for get and put operations)
        Space Complexity: O(N) (stores up to `capacity` items)
        """
        self.cache = OrderedDict()  # Ordered dictionary for maintaining order
        self.capacity = capacity  # Maximum number of items in cache

    def get(self, key: int) -> int:
        """
        Returns the value associated with the key if it exists, otherwise returns -1.
        Also moves the key to the front to mark it as recently used.
        Time Complexity: O(1)
        """
        if key not in self.cache:
            return -1  # Key not found

        # Move the key to the front (most recently used)
        self.cache.move_to_end(key, last=False)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        Adds a key-value pair to the cache.
        If the cache exceeds capacity, removes the least recently used (LRU) item.
        Time Complexity: O(1)
        """
        if key in self.cache:
            # Move key to the front and update value
            self.cache.move_to_end(key, last=False)
            self.cache[key] = value
        else:
            # If cache is full, remove the least recently used (last item)
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=True)  # Remove LRU (last item in OrderedDict)
            # Insert new key-value pair
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)  # Move to front

# Example Usage
cache = LRUCache(2)
cache.put(1, 100)
cache.put(2, 200)
print("Get 1:", cache.get(1))  # Output: 100 (Cache: {2: 200, 1: 100})
cache.put(3, 300)  # Removes key 2 (LRU)
print("Get 2:", cache.get(2))  # Output: -1 (Not found)
print("Get 3:", cache.get(3))  # Output: 300 (Cache: {1: 100, 3: 300})
