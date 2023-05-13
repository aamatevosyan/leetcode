from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        result = amount

        coins = sorted(coins, key=lambda x: -x)
        visited = set([0])

        q = deque()
        q.append((0, 0))
        visited.add(0)

        while q:
            curr, cnt = q.popleft()

            for coin in coins:
                if curr + coin == amount:
                    return cnt + 1
                elif curr + coin > amount or curr + coin in visited:
                    continue
                else:
                    q.append((curr + coin, cnt + 1))
                    visited.add(curr + coin)

        return -1