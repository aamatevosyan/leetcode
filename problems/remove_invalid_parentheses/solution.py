from collections import deque

class Solution:
    def isParenthesis(self, c: str) -> bool:
        return c in ('(', ')')
    
    def isValidString(self, s: str) -> bool:
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
            
            if cnt < 0 or cnt > (len(s) // 2):
                return False
        
        return cnt == 0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        if len(s) == 0:
            return
        
        visited = set()
        q = deque()
        result = []
        found = False

        q.append(s)
        visited.add(str)

        while q:
            s = q.popleft()

            if self.isValidString(s):
                result.append(s)
                found = True
            
            if found:
                continue
            
            for i in range(len(s)):
                if not self.isParenthesis(s[i]):
                    continue
                
                tmp = s[:i] + s[i + 1:]

                if tmp not in visited:
                    visited.add(tmp)
                    q.append(tmp)
        
        return result
                
