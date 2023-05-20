from dataclasses import dataclass

@dataclass
class Node:
    key: str
    value: int
    prev: Optional['Node'] = None
    next: Optional['None'] = None

class LRUCache:
    HEAD_KEY = '*'
    TAIL_KEY = '*'

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        
        self.head = Node(self.HEAD_KEY, 0)
        self.tail = Node(self.TAIL_KEY, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        
        node = self.store[key]

        self._remove(node)
        self._add(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self._remove(self.store[key])
        
        node = Node(key=key, value=value)
        self._add(node)

        self.store[key] = node
    
        if len(self.store) > self.capacity:
            node_to_remove = self.tail.prev
            self._remove(node_to_remove)

            self.store.pop(node_to_remove.key)
    
    def _add(self, node: Node) -> None:
        next_node = self.head.next
        prev_node = self.head

        prev_node.next = node
        next_node.prev = node
        
        node.next = next_node
        node.prev = prev_node
    
    def _remove(self, node: Node) -> None:
        next_node = node.next
        prev_node = node.prev

        prev_node.next = next_node
        next_node.prev = prev_node
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)