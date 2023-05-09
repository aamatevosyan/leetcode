# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = 0

    def getEdgeCount(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left, right = self.getEdgeCount(root.left), self.getEdgeCount(root.right)

        self.answer = max(self.answer, left + right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getEdgeCount(root)
        return self.answer