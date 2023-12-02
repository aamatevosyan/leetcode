# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, nums: List[int], l: int, r: int) -> Optional[TreeNode]:
        if l > r:
            return None
        
        max_ind = l
        for i in range(l + 1, r + 1):
            if nums[i] > nums[max_ind]:
                max_ind = i
        
        root = TreeNode(nums[max_ind])
        root.left = self.build(nums, l, max_ind - 1)
        root.right = self.build(nums, max_ind + 1, r)

        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums, 0, len(nums) - 1)
        