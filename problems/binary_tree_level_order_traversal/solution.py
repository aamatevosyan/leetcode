from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level_order, q = [], deque([root])

        while q:
            level_order.append([])
            curr = deque()

            for node in q:
                level_order[-1].append(node.val)

                if node.left:
                    curr.append(node.left)
                
                if node.right:
                    curr.append(node.right)

            q = curr
        
        return level_order
        