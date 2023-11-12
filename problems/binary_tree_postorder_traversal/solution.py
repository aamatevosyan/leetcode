# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)]
        postorder = []

        while stack:
            curr, visited = stack.pop()
            if not curr:
                continue
            
            if visited:
                postorder.append(curr.val)
                continue
            
            stack.append((curr, True))
            stack.append((curr.right, False))
            stack.append((curr.left, False))
        
        return postorder