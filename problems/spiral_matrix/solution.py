MARK = 1000

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        result = []
        directions = (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        )

        i, j, dirIndex = 0, 0, 0
        n, m = len(matrix), len(matrix[0])

        while i >= 0 and i < n and j >= 0 and j < m and matrix[i][j] != MARK:
            result.append(matrix[i][j])
            matrix[i][j] = MARK

            di, dj = directions[dirIndex]
            _di, _dj = i + di, j + dj

            if _di < 0 or _di >= n or _dj < 0 or _dj >= m or matrix[_di][_dj] == MARK:
                dirIndex = (dirIndex + 1) % len(directions)
                
                di, dj = directions[dirIndex]
                _di, _dj = i + di, j + dj
            
            i, j = _di, _dj

        return result