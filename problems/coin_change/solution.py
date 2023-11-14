class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [math.inf] * amount

        for coin in coins:
            for charge in range(coin, amount + 1):
                dp[charge] = min(dp[charge], dp[charge - coin] + 1)
        
        return -1 if isinf(dp[amount]) else dp[amount]
        