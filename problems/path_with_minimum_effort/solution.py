class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        seen = [[False] * m for _ in range(n)]
        
        q = [(0, 0, 0)]
        max_effort = 0

        while q:
            e, i, j = heappop(q)
            
            max_effort = max(e, max_effort)
            seen[i][j] = True

            if i == n - 1 and j == m - 1:
                break

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                _i, _j = di + i, dj + j

                if _i < 0 or _i >= n or _j < 0 or _j >= m or seen[_i][_j]:
                    continue
                
                _e = abs(heights[i][j] - heights[_i][_j])
                heappush(q, (_e, _i, _j))
        
        return max_effort