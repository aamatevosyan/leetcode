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
        
        result = []

        q = deque()
        q.append((0, root))

        while q:
            level, el = q.popleft()

            while len(result) < level + 1:
                result.append([])
            
            result[level].append(el.val)

            if el.left:
                q.append((level + 1, el.left))
            
            if el.right:
                q.append((level + 1, el.right))

        return result           