from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))

        q = deque()
        q.append((sr, sc))

        initialColor = image[sr][sc]

        while q:
            x, y = q.pop()
            if image[x][y] != initialColor or image[x][y] == color:
                continue

            image[x][y] = color

            for dx, dy in directions:
                _x, _y = x + dx, y + dy

                if 0 <= _x < n and 0 <= _y < m:
                    q.append((_x, _y))

        return image
