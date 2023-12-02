# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: Optional[TreeNode], memo: Dict[str, int], result: List[Optional[TreeNode]]) -> str:
        if not root:
            return "#"
        
        left = self.traverse(root.left, memo, result)
        right = self.traverse(root.right, memo, result)

        sub_tree = f"{left},{right},{root.val}"
        freq = memo.get(sub_tree, 0)

        if freq == 1:
            result.append(root)
        
        memo[sub_tree] = freq + 1

        return sub_tree

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result, memo = [], {}

        self.traverse(root, memo, result)

        return result
        