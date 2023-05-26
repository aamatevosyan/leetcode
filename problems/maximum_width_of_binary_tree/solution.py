from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q, max_width = deque([(1, root)]), 0

        while q:
            _len, start_index, _index = len(q), q[0][0], q[0][0]

            for _ in range(_len):
                _index, node = q.popleft()

                if node.left:
                    q.append((_index * 2, node.left))
                
                if node.right:
                    q.append((_index * 2 + 1, node.right))
            
            max_width = max(max_width, _index - start_index + 1)
        
        return max_width

