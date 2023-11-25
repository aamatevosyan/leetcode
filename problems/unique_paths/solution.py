class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] + [1] + [0] * (n - 1)
        
        for i in range(1, m + 1):
            curr = [0] * (n + 1)

            for j in range(1, n + 1):
                curr[j] = dp[j] + curr[j - 1]
            
            dp = curr
        
        return dp[n]
        