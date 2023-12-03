class Solution:
    def __init__(self):
        self.result = 0

    def is_valid(self, board: List[List[str]], row: int, col: int) -> bool:
        n = len(board)
        for i in range(n):
            if board[i][col] == "Q":
                return False
        
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1
    
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        
        return True

    def backtrack(self, board: List[List[str]], row: int):
        if row == len(board):
            self.result += 1
            return
        
        for col in range(len(board)):
            if not self.is_valid(board, row, col):
                continue
            
            board[row][col] = 'Q'
            self.backtrack(board, row + 1)
            board[row][col] = '.'

    def totalNQueens(self, n: int) -> int:
        self.backtrack([['.'] * n for _ in range(n)], 0)

        return self.result
        