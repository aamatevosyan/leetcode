class Solution:
    EMPTY, FRESH, ROTTEN = 0, 1, 2
    DIRECTIONS = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        n, m = len(grid), len(grid[0])
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == self.ROTTEN:
                    q.append((i, j))
                    grid[i][j] = self.EMPTY
        
        result = 0

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                for di, dj in self.DIRECTIONS:
                    _i, _j = di + i, dj + j

                    if _i >= 0 and _i < n and _j >= 0 and _j < m and grid[_i][_j] == self.FRESH:
                        grid[_i][_j] = self.EMPTY
                        q.append((_i, _j))
            
            result += 1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == self.FRESH:
                    return -1

        return result - 1 if result > 0 else 0