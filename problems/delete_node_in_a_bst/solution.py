# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key:
            if not root.left:
                return root.right
            
            if not root.right:
                return root.left
            
            min_node = self.min_node(root.right)
            root.right = self.deleteNode(root.right, min_node.val)

            min_node.left = root.left
            min_node.right = root.right
            
            root = min_node
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        return root
    
    def min_node(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        while root.left:
            root = root.left
        
        return root