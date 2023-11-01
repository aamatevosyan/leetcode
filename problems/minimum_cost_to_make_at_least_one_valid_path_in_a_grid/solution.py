from collections import deque

class Solution:
    DIRECTIONS = [
        (0, 1, 1),
        (0, -1, 2),
        (1, 0, 3),
        (-1, 0, 4),
    ]

    def minCost(self, grid: List[List[int]]) -> int:
        q, m, n = deque([(0, 0, 0)]), len(grid), len(grid[0])
        dist = [[m * n + 1 for _ in range(n)] for _ in range(m)]
        
        dist[0][0] = 0

        while q:
            cost, i, j = q.popleft()

            if cost > dist[i][j]:
                continue

            if i == m - 1 and j == n - 1:
                break
            
            for d_i, d_j, dir in self.DIRECTIONS:
                _i, _j = i + d_i, j + d_j

                if _i < 0 or _i >= m or _j < 0 or _j >= n:
                    continue
                
                _cost = cost if grid[i][j] == dir else 1 + cost

                if _cost >= dist[_i][_j]:
                    continue
                
                dist[_i][_j] = _cost

                if _cost == cost:
                    q.appendleft((_cost, _i, _j))
                else:
                    q.append((_cost, _i, _j))
        
        return dist[m - 1][n - 1]


        