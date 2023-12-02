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
        postorder: List[int], postorder_start: int, postorder_end: int, 
        inorder: List[int], inorder_start: int, inorder_end: int
    ) -> Optional[TreeNode]:
        if postorder_start > postorder_end:
            return None

        root = TreeNode(postorder[postorder_end])

        inorder_root_ind = inorder_map[root.val]
        left_size = inorder_root_ind - inorder_start

        root.left = self.build(
            inorder_map,
            postorder, postorder_start, postorder_start + left_size - 1,
            inorder, inorder_start, inorder_root_ind - 1,
        )

        root.right = self.build(
            inorder_map,
            postorder, postorder_start + left_size, postorder_end - 1,
            inorder, inorder_root_ind + 1, inorder_end
        )

        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.build(
            { num: i for i, num in enumerate(inorder) },
            postorder, 0, len(postorder) - 1,
            inorder, 0, len(inorder) - 1
        )