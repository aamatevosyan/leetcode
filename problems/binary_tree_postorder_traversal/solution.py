# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        curr, st, postorder = root, [root], []

        while st:
            curr = st.pop()
            postorder.append(curr.val)
            
            if curr.left:
                st.append(curr.left)
            
            if curr.right:
                st.append(curr.right)
        
        return postorder[::-1]