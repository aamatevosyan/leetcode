from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        right_side_view, q = [], deque([root])

        while q:
            curr = deque([])
            right_side_view.append(q[0].val)

            for node in q:
                if node.right:
                    curr.append(node.right)
                
                if node.left:
                    curr.append(node.left)
            
            q = curr
        
        return right_side_view

        