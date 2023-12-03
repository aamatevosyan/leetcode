# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        diameter = left_height + right_height

        if diameter > self.diameter:
            self.diameter = diameter
        
        return 1 + max(left_height, right_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getHeight(root)

        return self.diameter
        