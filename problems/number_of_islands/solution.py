class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        m, n, count = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1':
                    continue
                
                self.dfs(grid, m, n, i, j)
                count += 1
        
        return count

    def dfs(self, grid, m, n, i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            return
        
        grid[i][j] = 'X'

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        for _i, _j in directions:
            self.dfs(grid, m, n, i + _i, j + _j)
        
