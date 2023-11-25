class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount

        for coin in coins:
            for change in range(coin, amount + 1):
                dp[change] = min(dp[change], dp[change - coin] + 1)
        
        return -1 if dp[amount] > amount else dp[amount]

        