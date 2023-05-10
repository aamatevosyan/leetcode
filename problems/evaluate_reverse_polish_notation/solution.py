from collections import deque

class Solution:
    def __init__(self):
        self.q = deque()

    def isOperator(self, op: str) -> bool:
        return op in ('+', '-', '*', '/')
    
    def performOperator(self, op: str, a: int, b: int) -> int:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            return trunc(a / b)
    
    def calc(self, op: str):
        if self.isOperator(op):
            b = self.q.pop()
            a = self.q.pop()

            c = self.performOperator(op, a, b)
        else:
            c = int(op)
        
        self.q.append(c)


    def evalRPN(self, tokens: List[str]) -> int:
        for token in tokens:
            self.calc(token)
        
        return self.q.pop()