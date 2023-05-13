EMPTY, FRESH, ROTTEN = 0, 1, 2

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        n, m = len(grid), len(grid[0])
        q = deque()
        visited = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] != ROTTEN:
                    continue
                
                q.append((0, (i, j)))
                visited.add((i, j))
        
        directions = (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        )
        
        result = 0

        while q:
            order, (i, j) = q.popleft()
            result = order

            for di, dj in directions:
                _i, _j = di + i, dj + j

                if _i >= 0 and _i < n and _j >= 0 and _j < m and grid[_i][_j] == FRESH and not (_i, _j) in visited:
                    visited.add((_i, _j))
                    grid[_i][_j] = ROTTEN

                    q.append((order + 1, (_i, _j)))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == FRESH:
                    return -1

        return result