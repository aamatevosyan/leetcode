class Solution:
    def knapsack(self, nums: List[int], target: int, total: int):
        dp = [1] + [0] * total

        for num in nums:
            for j in range(total, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[target]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total or (total + target) & 1:
            return 0
        
        return self.knapsack(nums, (total + target) // 2, total)
        