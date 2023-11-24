class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_ind = bisect_left(nums, target)
        if left_ind == len(nums) or nums[left_ind] != target:
            return [-1, -1]
        
        right_ind = bisect_right(nums, target) - 1
        
        return[left_ind, right_ind]
        