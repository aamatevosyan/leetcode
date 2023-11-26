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
        visited = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == self.ROTTEN:
                    q.append((i, j))
                    visited.add((i, j))
        
        result = -1

        while q:
            curr = deque([])
            result += 1

            for i, j in q:
                for di, dj in self.DIRECTIONS:
                    _i, _j = di + i, dj + j

                    if _i >= 0 and _i < n and _j >= 0 and _j < m and grid[_i][_j] == self.FRESH and not (_i, _j) in visited:
                        visited.add((_i, _j))
                        grid[_i][_j] = self.ROTTEN

                        curr.append((_i, _j))

            q = curr
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == self.FRESH:
                    return -1

        return result if result != -1 else 0