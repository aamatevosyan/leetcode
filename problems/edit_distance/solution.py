class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        n, m = len(word1), len(word2)
        dp = list(range(m + 1))

        for i in range(1, n + 1):
            curr = [i] + [0] * m

            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = dp[j - 1]
                else:
                    curr[j] = min(
                        dp[j - 1],
                        dp[j],
                        curr[j - 1]
                    ) + 1
            
            dp = curr
        
        return dp[m]
        