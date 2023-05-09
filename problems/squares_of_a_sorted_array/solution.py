class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        l, r, i = 0, len(nums) - 1, len(nums) - 1

        while i >= 0:
            if abs(nums[l]) < abs(nums[r]):
                result[i] = nums[r] * nums[r]
                r -= 1
            else:
                result[i] = nums[l] * nums[l]
                l += 1
            
            i -= 1
        
        return result
