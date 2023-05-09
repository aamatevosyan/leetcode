class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, ans = 0, -10000
        for num in nums:
            curr = max(num, curr + num)
            ans = max(ans, curr)
        
        return ans