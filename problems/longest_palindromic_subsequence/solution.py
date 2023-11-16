class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            curr = [0] * i + [1] + [0] * (n - i - 1)

            for j in range(i + 1, n):

                if s[i] == s[j]:
                    curr[j] = 2 + dp[j - 1]
                else:
                    curr[j] = max(dp[j], curr[j - 1])
            
            dp = curr

        return dp[-1]