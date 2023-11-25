class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n
        max_len = max(map(len, wordDict))
        
        for i in range(n):
            for j in range(i, max(i - max_len, -1), -1):
                if dp[j] and s[j : i + 1] in wordDict:
                    dp[i + 1] = True
                    break
        
        return dp[n]
                    
        