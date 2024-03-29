# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr, small, large = root, min(p.val, q.val), max(p.val, q.val)

        while curr:
            if curr.val > large:
                curr = curr.left
            elif curr.val < small:
                curr = curr.right
            else:
                break
        
        return curr
        
        