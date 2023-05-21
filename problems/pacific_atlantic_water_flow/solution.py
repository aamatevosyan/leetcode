class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m, result = len(heights), len(heights[0]), []
        atlantic = [[False] * m for _ in range(n)] 
        pacific = [[False] * m for _ in range(n)]

        directions = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        )

        def bfs(visited, i, j):
            q = deque([(i, j)])

            while q:
                i, j = q.popleft()

                if visited[i][j]:
                    continue
                
                visited[i][j] = True

                if atlantic[i][j] and pacific[i][j]:
                    result.append([i, j])
                
                for di, dj in directions:
                    _di, _dj = di + i, dj + j

                    if _di >= 0 and _di < n and _dj >= 0 and _dj < m and heights[_di][_dj] >= heights[i][j]:
                        q.append((_di, _dj))

        for i in range(n):
            bfs(pacific, i, 0)
            bfs(atlantic, i, m - 1)

        for i in range(m):
            bfs(pacific, 0, i)
            bfs(atlantic, n - 1, i)
        
        return result
                


