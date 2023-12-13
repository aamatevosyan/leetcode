# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result, q = [], deque([root] if root else [])

        while q:
            result.append(q[0].val)

            for _ in range(len(q)):
                node = q.popleft()
                
                if node.right:
                    q.append(node.right)
                
                if node.left:
                    q.append(node.left)
        
        return result