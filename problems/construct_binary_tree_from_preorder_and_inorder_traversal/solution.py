# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(
        self, 
        preorder: List[int], 
        inorder: List[int], 
        inorderMap: Dict[str, int],
        preLeft: int,
        preRight: int,
        inLeft: int,
        inRight: int,
    ) -> Optional[TreeNode]:
        if preLeft > preRight:
            return None
        
        rootVal = preorder[preLeft]
        rootValInOrderIndex = inorderMap[rootVal]
        leftSideLen = rootValInOrderIndex - inLeft

        root = TreeNode()
        root.val = rootVal
        root.left = self.build(
            preorder, inorder, inorderMap, preLeft + 1, preLeft + leftSideLen, inLeft, rootValInOrderIndex - 1, 
        )

        root.right = self.build(
            preorder, inorder, inorderMap, preLeft + 1 + leftSideLen, preRight, rootValInOrderIndex + 1, inRight, 
        )

        return root


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {}

        for i, v in enumerate(inorder):
            inorderMap[v] = i

        return self.build(preorder, inorder, inorderMap, 0, len(preorder) - 1, 0, len(inorder) - 1)