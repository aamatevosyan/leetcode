class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        n, m, max_len = len(matrix), len(matrix[0]), 0
        dp, prev = [0] * (m + 1), 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                curr = dp[j]

                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(prev, dp[j - 1], dp[j]) + 1
                    max_len = max(max_len, dp[j])
                else:
                    dp[j] = 0

                prev = curr

        return max_len ** 2
