# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidNode(self, node: Optional[TreeNode], lower: int, upper: int) -> bool:
        if not node:
            return True
        
        val = node.val
        if val <= lower or val >= upper:
            return False
        
        if not self.isValidNode(node.left, lower, val):
            return False
        
        if not self.isValidNode(node.right, val, upper):
            return False
        
        return True
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isValidNode(root, float('-inf'), float('inf'))