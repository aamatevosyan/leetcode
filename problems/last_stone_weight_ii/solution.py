class Solution:
    def knapsack(self, stones: List[int], total: int):
        goal = total // 2
        dp = [True] + [False] * goal

        for stone in stones:
            for j in range(goal, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]
        
        for i in range(goal, -1, -1):
            if dp[i]:
                return (total - i) - i

    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        
        return self.knapsack(stones, total)
        