class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [0] * n

        for i in range(n):
            curr = [math.inf] * n
            
            for j in range(n):
                curr[j] = min(curr[j], dp[j] + matrix[i][j])
                
                if j - 1 >= 0:
                    curr[j] = min(curr[j], dp[j - 1] + matrix[i][j])
                
                if j + 1 < n:
                    curr[j] = min(curr[j], dp[j + 1] + matrix[i][j])
            
            dp = curr
        
        return min(dp)
        