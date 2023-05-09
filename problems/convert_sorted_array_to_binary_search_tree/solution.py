# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedToBST(self, nums: List[int], l: int, r: int) -> Optional[TreeNode]:
        if l > r:
            return None
        
        m = (r - l) // 2 + l
        
        return TreeNode(
            val=nums[m],
            left=self.sortedToBST(nums, l, m - 1),
            right=self.sortedToBST(nums, m + 1, r),
        )

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sortedToBST(nums, 0, len(nums) - 1)