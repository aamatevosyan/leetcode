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
        
        q, visited, current_steps = deque([(0, 0, k)]), set(), -1

        while q:
            _q = deque()
            current_steps += 1

            while q:
                i, j, available_steps = q.popleft()

                if i == m - 1 and j == n - 1:
                    return current_steps
                
                for d_i, d_j in self.DIRECTIONS:
                    _i, _j = i + d_i, j + d_j

                    if _i < 0 or _i >= m or _j < 0 or _j >= n:
                        continue
                    
                    if available_steps - grid[_i][_j] < 0:
                        continue

                    step = (_i, _j, available_steps - grid[_i][_j])
                    
                    if step in visited:
                        continue
                    
                    visited.add(step)
                    _q.append(step)
            
            q = _q

        return -1
        
        