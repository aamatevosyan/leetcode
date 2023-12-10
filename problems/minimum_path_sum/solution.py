class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [0] * (m + 1)
        
        for i in range(1, m + 1):
            dp[i] = dp[i - 1] + grid[0][i - 1]

        for i in range(2, n + 1):
            curr = [0] * (m + 1)
            curr[1] = dp[1] + grid[i - 1][0]

            for j in range(2, m + 1):
                curr[j] = min(dp[j], curr[j - 1]) + grid[i - 1][j - 1]

            dp = curr

        return dp[m]
                
        