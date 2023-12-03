class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def is_palindrome(self, s: str, lo: int, hi: int) -> bool:
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True

    def backtrack(self, i: int, s: str):
        if i == len(s):
            self.result.append(self.path[:])
            return
        
        for j in range(i, len(s)):
            if not self.is_palindrome(s, i, j):
                continue
            
            self.path.append(s[i:j + 1])
            self.backtrack(j + 1, s)
            self.path.pop()
    
    def partition(self, s: str) -> List[List[str]]:
        self.backtrack(0, s)

        return self.result
        