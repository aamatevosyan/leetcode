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
        
        for child in root.children:
            self.helper(child, result)
        
        result.append(root.val)

    def postorder(self, root: 'Node') -> List[int]:
        result = []

        self.helper(root, result)

        return result
        