# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q, depth = deque([root]), 0

        while q:
            depth += 1
            sz = len(q)

            for _ in range(sz):
                node = q.popleft()

                if not node.left and not node.right:
                    return depth
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

        