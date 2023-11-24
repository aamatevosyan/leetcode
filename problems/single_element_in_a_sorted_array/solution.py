class Solution:
    def is_left_idx(self, nums: List[int], idx: int) -> bool:
        if idx == len(nums) - 1:
            return True
        
        if idx % 2 == 0:
            return nums[idx] != nums[idx + 1]
        else:
            return nums[idx] != nums[idx - 1]

    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            
            if self.is_left_idx(nums, m):
                r = m - 1
            else:
                l = m + 1
        
        return nums[l]
        