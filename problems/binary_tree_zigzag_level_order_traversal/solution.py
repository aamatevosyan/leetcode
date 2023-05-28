from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q, result, isReversed = deque([root]), [[root.val]], True

        while q:
            _len, _levelNodes = len(q), []
            
            if isReversed:
                _pop, _append = q.pop, q.appendleft
            else:
                _pop, _append = q.popleft, q.append
            
            for i in range(_len):
                node = _pop()
                children = (
                    [node.left, node.right] if not isReversed 
                    else [node.right, node.left]
                )
                
                for child in children:
                    if not child:
                        continue

                    _levelNodes.append(child.val)
                    _append(child)
            
            if _levelNodes:
                result.append(_levelNodes)
            
            isReversed = not isReversed
        
        return result
        
