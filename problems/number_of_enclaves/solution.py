class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        m, n, cnt = len(grid), len(grid[0]), 0

        for i in range(m):
            self.dfs(grid, m, n, i, 0)
            self.dfs(grid, m, n, i, n - 1)
        
        for j in range(n):
            self.dfs(grid, m, n, 0, j)
            self.dfs(grid, m, n, m - 1, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
        
        return cnt

    def dfs(self, grid, m, n, i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return
        
        grid[i][j] = 0

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        for _i, _j in directions:
            self.dfs(grid, m, n, i + _i, j + _j)
        