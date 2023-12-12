from collections import deque

class Solution:
    DIRECTIONS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]
    
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        if k >= m + n - 2:
            return m + n - 2
        
        q, visited, steps = deque([(0, 0, k)]), set(), 0

        while q:
            for _ in range(len(q)):
                i, j, steps_left = q.popleft()
                                
                for d_i, d_j in self.DIRECTIONS:
                    _i, _j = i + d_i, j + d_j

                    if _i < 0 or _i >= m or _j < 0 or _j >= n:
                        continue
                    
                    if steps_left - grid[_i][_j] < 0:
                        continue
                    
                    if _i == m - 1 and _j == n - 1:
                        return steps + 1

                    option = (_i, _j, steps_left - grid[_i][_j])
                    
                    if option in visited:
                        continue
                    
                    visited.add(option)
                    q.append(option)
            
            steps += 1

        return -1
        
        