"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def helper(self, root: 'Node', result: List[int]):
        if not root:
            return
        
        result.append(root.val)
        for child in root.children:
            self.helper(child, result)
    
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        self.helper(root, result)

        return result
        