# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode], seen: Set[int], k: int):
        if not root:
            return False
        
        if (k - root.val) in seen:
            return True
        
        seen.add(root.val)

        return self.helper(root.left, seen, k) or self.helper(root.right, seen, k)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        return self.helper(root, seen, k)
        