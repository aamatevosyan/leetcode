from collections import deque

class Solution:
    def getOposite(self, s: str):
        maping = {
            '(': ')',
            ')': '(',
            '[': ']',
            ']': '[',
            '{': '}',
            '}': '{'
        }

        return maping[s]

    def isOpen(self, s: str):
        return s in ['(', '{', '[']

    def isValid(self, s: str) -> bool:
        q = deque()

        for el in s:
            if self.isOpen(el):
                q.append(el)
            else:
                if len(q) == 0:
                    return False
                    
                last = q.pop()
                if last != self.getOposite(el):
                    return False
        
        return len(q) == 0
