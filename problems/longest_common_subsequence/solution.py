class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        n, m = len(text1), len(text2)
        dp = [0] * (m + 1)

        for i in range(1, n + 1):
            curr = [0] * (m + 1)

            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = 1 + dp[j - 1]
                else:
                    curr[j] = max(dp[j], curr[j - 1])
            
            dp = curr
        
        return dp[m]
        