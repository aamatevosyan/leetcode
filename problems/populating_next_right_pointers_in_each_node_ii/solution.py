from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q, right_most = deque([root]), root

        while q:
            right_most, n = None, len(q)

            for _ in range(n):
                node = q.popleft()
                
                node.next = right_most
                right_most = node

                if node.right:
                    q.append(node.right)
                
                if node.left:
                    q.append(node.left)

        return root

        