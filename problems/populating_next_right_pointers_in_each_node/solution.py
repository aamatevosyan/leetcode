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
    def helper(self, p: 'Node', q: 'Node'):
        if not p or not q:
            return

        p.next = q
        self.helper(p.left, p.right)
        self.helper(q.left, q.right)
        self.helper(p.right, q.left)

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        self.helper(root.left, root.right)

        return root