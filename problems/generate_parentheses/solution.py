from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, q = [], deque([(0, 0, "")]) 

        while q:
            opened, closed, curr = q.pop()
            if opened == n and closed == n:
                result.append(curr)
                continue
            
            if opened < n:
                q.append((opened + 1, closed, curr + "("))
            
            if closed < opened:
                q.append((opened, closed + 1, curr + ")"))

        return result
        