from collections import deque
from sortedcontainers import SortedSet

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        q, roots, deletes = deque([(root, False)]), [], SortedSet(to_delete)

        while q:
            node, parent_has_parent = q.popleft()
            has_parent = node.val not in deletes

            if not parent_has_parent and has_parent:
                roots.append(node)

            if not has_parent:
                deletes.remove(node.val)
            
            if node.left:
                q.append((node.left, has_parent))
                
                if node.left.val in deletes:
                    node.left = None
            
            if node.right:
                q.append((node.right, has_parent))

                if node.right.val in deletes:
                    node.right = None
        
        return roots
        