class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target

        for curr in range(1, target + 1):
            for num in sorted(nums):
                if num > curr:
                    break
                
                dp[curr] += dp[curr - num]
        
        return dp[target]
        