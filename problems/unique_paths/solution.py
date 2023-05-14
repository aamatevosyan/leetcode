from collections import deque

MARK = 0

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = (
            (0, 1),
            (1, 0),
        )

        dp = [[MARK for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        q = deque()
        q.append((0, 0))

        while q:
            i, j = q.popleft()

            for di, dj in directions:
                _di, _dj = di + i, dj + j
                if _di >= 0 and _di < m and _dj >= 0 and _dj < n:
                    if dp[_di][_dj] == MARK:
                        q.append((_di, _dj))

                    dp[_di][_dj] += dp[i][j]

        return dp[m - 1][n - 1]