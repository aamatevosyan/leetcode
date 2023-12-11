class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr, result = 0, [0] * len(nums)

        for i, num in enumerate(nums):
            curr += num
            result[i] = curr
        
        return result