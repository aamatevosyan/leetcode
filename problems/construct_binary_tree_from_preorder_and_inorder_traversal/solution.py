# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(
        self,
        inorder_map: Dict[int, int],
        preorder: List[int], preorder_start: int, preorder_end: int, 
        inorder: List[int], inorder_start: int, inorder_end: int
    ) -> Optional[TreeNode]:
        if preorder_start > preorder_end:
            return None

        root = TreeNode(preorder[preorder_start])

        inorder_root_ind = inorder_map[root.val]
        left_size = inorder_root_ind - inorder_start

        root.left = self.build(
            inorder_map,
            preorder, preorder_start + 1, preorder_start + left_size,
            inorder, inorder_start, inorder_root_ind - 1,
        )

        root.right = self.build(
            inorder_map,
            preorder, preorder_start + left_size + 1, preorder_end,
            inorder, inorder_root_ind + 1, inorder_end
        )

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(
            { num: i for i, num in enumerate(inorder) },
            preorder, 0, len(preorder) - 1,
            inorder, 0, len(inorder) - 1
        )
        