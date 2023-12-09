# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    def traverse(self, root: Optional[TreeNode]):
        if not root:
            return
        
        self.traverse(root.right)
        
        self.sum += root.val
        root.val = self.sum

        self.traverse(root.left)
        

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)

        return root
        