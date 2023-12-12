class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total, left = sum(nums), 0

        for i, num in enumerate(nums):
            if left == total - left - num:
                return i
            
            left += num
        
        return -1

        