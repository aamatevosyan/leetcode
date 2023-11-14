class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount

        for coin in coins:
            for charge in range(coin, amount + 1):
                dp[charge] += dp[charge - coin]
        
        return dp[amount]
        