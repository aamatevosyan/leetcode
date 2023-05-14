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
        
        q = deque()
        result = []
        q.append((0, root))

        currentMax = -1

        while q:
            level, node = q.popleft()

            if currentMax < level:
                result.append(node.val)
                currentMax = level
            
            if node.right:
                q.append((level + 1, node.right))
            
            if node.left:
                q.append((level + 1, node.left))
                

        return result