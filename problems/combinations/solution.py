class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(n, k, 1)

        return self.result
    
    def backtrack(self, n: int, k: int, start: int) -> None:
        if len(self.path) == k:
            self.result.append(self.path[:])
            return

        for i in range(start, n + 1):
            self.path.append(i)

            self.backtrack(n, k, i + 1)
            
            self.path.pop()