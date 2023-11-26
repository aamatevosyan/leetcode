# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_valid(self, root: Optional[TreeNode], min_value: int, max_value: int) -> bool:
        if not root:
            return True

        if root.val <= min_value or root.val >= max_value:
            return False
        
        return self.is_valid(root.left, min_value, root.val) and self.is_valid(root.right, root.val, max_value)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid(root, -math.inf, math.inf)
        