from collections import deque, defaultdict

class Solution:
    def helper(self, board: List[List[str]], word: str, i: int, j: int, n: int, m: int) -> bool:
        q = deque([(set([(i, j)]), 0, (i, j))])

        directions = (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        )

        while q:
            visited, ind, (_i, _j) = q.popleft()

            for di, dj in directions:
                _di, _dj = _i + di, _j + dj

                if ind + 1 == len(word):
                    return True

                if _di < 0 or _dj < 0 or _di >= n or _dj >= m or (_di, _dj) in visited or word[ind + 1] != board[_di][_dj]:
                    continue
                
                q.append((visited.union(set([(_di, _dj)])), ind + 1, (_di, _dj)))

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        n, m = len(board), len(board[0])

        wordCount = defaultdict(int)
        for c in word:
            wordCount[c] += 1
        
        for i in range(n):
            for j in range(m):
                c = board[i][j]

                wordCount[c] -= 1
        
        for c in wordCount:
            if wordCount[c] > 0:
                return False
        

        for i in range(n):
            for j in range(m):
                if (
                    board[i][j] == word[0] 
                    and self.helper(
                        board,
                        word,
                        i,
                        j,
                        n,
                        m
                    )
                ):
                    return True


        return False