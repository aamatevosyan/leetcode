from collections import deque

class Solution:
    def transform(self, s: str):
        q = deque()

        for c in s:
            if c == '#' and q:
                q.pop()
            else:
                q.append(c)
        
        return q

    def backspaceCompare(self, s: str, t: str) -> bool:
        s_q, t_q = self.transform(s), self.transform(t)

        while s_q and t_q:
            if s_q.pop() != t_q.pop():
                return False

        while s_q:
            if s_q.pop() != '#':
                return False

        while t_q:
            if t_q.pop() != '#':
                return False
        
        return True