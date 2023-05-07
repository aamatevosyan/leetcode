from collections import deque

class Solution:
    def getOposite(self, s: str):
        maping = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        return maping[s]

    def isOpen(self, s: str):
        return s in ('(', '{', '[')

    def isValid(self, s: str) -> bool:
        q = deque()

        for el in s:
            if self.isOpen(el):
                q.append(el)
                continue
            
            if not q or q.pop() != self.getOposite(el):
                return False
        
        return not q
