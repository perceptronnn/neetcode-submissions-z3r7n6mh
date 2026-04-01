class ListNode:
    """Doubly linked list node for LRU cache implementation."""
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    LRU Cache implementation using HashMap + Doubly Linked List.
    
    Time Complexity: O(1) for both get() and put()
    Space Complexity: O(capacity)
    """
    
    def __init__(self, capacity: int):
        """
        Initialize LRU cache with given capacity.
        
        Args:
            capacity: Maximum number of key-value pairs to store
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
            
        self.capacity = capacity
        self.cache = {}  # key -> ListNode mapping
        
        # Create dummy head and tail for easier manipulation
        self.head = ListNode()  # Most recently used end
        self.tail = ListNode()  # Least recently used end
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        Get value by key. Mark as most recently used.
        
        Args:
            key: The key to look up
            
        Returns:
            The value if key exists, -1 otherwise
        """
        if key not in self.cache:
            return -1
            
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair. Mark as most recently used.
        
        Args:
            key: The key to insert/update
            value: The value to store
        """
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # Insert new key
            if len(self.cache) >= self.capacity:
                self._evict_lru()
            
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

    def _add_to_head(self, node: ListNode) -> None:
        """Add node right after head (most recently used position)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: ListNode) -> None:
        """Remove node from its current position in the list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node: ListNode) -> None:
        """Move existing node to head (mark as most recently used)."""
        self._remove_node(node)
        self._add_to_head(node)

    def _pop_tail(self) -> ListNode:
        """Remove and return the node before tail (least recently used)."""
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        return lru_node

    def _evict_lru(self) -> None:
        """Remove least recently used item from cache."""
        lru_node = self._pop_tail()
        del self.cache[lru_node.key]
