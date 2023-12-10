class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        m, n, area = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                
                area = max(area, self.dfs(grid, m, n, i, j))
        
        return area

    def dfs(self, grid, m, n, i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return 0
        
        grid[i][j] = 0

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        area = 1

        for _i, _j in directions:
            area += self.dfs(grid, m, n, i + _i, j + _j)
        
        return area