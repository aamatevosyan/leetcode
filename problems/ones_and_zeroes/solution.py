class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeroes = sum(1 if c == "0" else 0 for c in s)
            ones = len(s) - zeroes

            for i in range(m, zeroes - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeroes][j - ones] + 1)

        return dp[m][n] 
        