"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def clone(self, node: 'Node', cloned: Dict['Node', 'Node']):
        clone = Node(node.val)
        cloned[node] = clone

        for it in node.neighbors:
            if it not in cloned:
                clone.neighbors.append(self.clone(it, cloned))
            else:
                clone.neighbors.append(cloned[it])
        
        return clone

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        if not node.neighbors:
            return Node(node.val)
        
        cloned = {}

        return self.clone(node, cloned)