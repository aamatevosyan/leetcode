class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        nums.sort()

        for current_target in range(1, target + 1):
            for num in nums:
                if num <= current_target:
                    dp[current_target] += dp[current_target - num]
                else:
                    break
        
        return dp[target]
        