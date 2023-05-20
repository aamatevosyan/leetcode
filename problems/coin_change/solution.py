from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins = sorted(coins, key=lambda x: -x)
        memo = [-1] * (amount + 1)

        q = deque([0])
        memo[0] = 0

        while q:
            i = q.popleft()

            for coin in coins:
                if i + coin > amount or memo[i + coin] >= 0:
                    continue

                if i + coin == amount:
                    return memo[i] + 1 
                
                q.append(i + coin)
                memo[i + coin] = memo[i] + 1

        return -1