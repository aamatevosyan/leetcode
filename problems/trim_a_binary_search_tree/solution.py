from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trim(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val > high:
            return self.trim(root.left, low, high)
        elif root.val < low:
            return self.trim(root.right, low, high)
        
        root.left = self.trim(root.left, low, high)
        root.right = self.trim(root.right, low, high)
        
        return root
        
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        return self.trim(root, low, high)
        