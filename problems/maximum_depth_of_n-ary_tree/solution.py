from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        q, level = deque(), 0
        q.append(root)

        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
            
                for child in node.children:
                    q.append(child)
            
            level += 1
        
        return level