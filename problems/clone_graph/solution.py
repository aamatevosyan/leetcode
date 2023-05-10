from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        q = deque([node])
        cloned = [None] * 101
        cloned[node.val] = Node(val=node.val) 

        while q:
            _node = q.popleft()

            for child in _node.neighbors:
                if cloned[child.val] is None:
                    cloned[child.val] = Node(val=child.val)
                    q.append(child)

                cloned[_node.val].neighbors.append(cloned[child.val])

        return cloned[node.val]