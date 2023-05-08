# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.getHeight(
            root.left), self.getHeight(root.right)) + 1
    
    def isBalancedNodes(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        diff = abs(self.getHeight(root.left) - self.getHeight(root.right))

        if diff > 1:
            return False

        return self.isBalancedNodes(root.left) and self.isBalancedNodes(root.right)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedNodes(root)