class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()

        n, m = len(mat), len(mat[0])
        directions = (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        )

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1
        
        while q:
            i, j = q.popleft()

            for di, dj in directions:
                _i, _j = di + i, dj + j

                if _i < 0 or _i >= n or _j < 0 or _j >= m or mat[_i][_j] != -1:
                    continue
                
                mat[_i][_j] = mat[i][j] + 1
                q.append((_i, _j))
        
        return mat