class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if len(grid1) == 0:
            return 0

        m, n, cnt = len(grid1), len(grid1[0]), 0

        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    self.dfs(grid2, m, n, i, j)

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 0:
                    continue
                
                self.dfs(grid2, m, n, i, j)
                cnt += 1
        
        return cnt

    def dfs(self, grid, m, n, i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return
        
        grid[i][j] = 0

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        for _i, _j in directions:
            self.dfs(grid, m, n, i + _i, j + _j)