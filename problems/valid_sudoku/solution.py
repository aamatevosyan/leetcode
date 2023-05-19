class Solution:
    def isValid(self, board: List[List[str]], si: int, sj: int, n: int, m: int):
        visited = set()

        for i in range(si, si + n):
            for j in range(sj, sj + m):
                c = board[i][j]
                if c == '.':
                    continue

                if c in visited:
                    return False

                visited.add(c)
        
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        for i in range(N):
            if not self.isValid(board, i, 0, 1, 9):
                return False
            if not self.isValid(board, 0, i, 9, 1):
                return False

        for i in (0, 3, 6):
            for j in (0, 3, 6):
                if not self.isValid(board, i, j, 3, 3):
                    return False
        
        return True
