class Solution:
    def transpose(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
    def reflect(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            l, r = 0, len(matrix[0]) - 1

            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1


    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)

        