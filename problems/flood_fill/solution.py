class Solution:
    directions = ((0, 1), (0, -1), (-1, 0), (1, 0))

    def fill(self, image: List[List[int]], i: int, j: int, color: int, initial_color: int):
        n, m = len(image), len(image[0])
        image[i][j] = color
        
        for di, dj in self.directions:
             _i, _j = i + di, j + dj

             if _i < 0 or _i >= n or _j < 0 or _j >= m or image[_i][_j] != initial_color or image[_i][_j] == color:
                 continue
             
             self.fill(image, _i, _j, color, initial_color)
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] != color:
            self.fill(image, sr, sc, color, image[sr][sc])
        
        return image


        