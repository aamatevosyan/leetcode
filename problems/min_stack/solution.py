class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack or val <= self.getMin():
            self.minStack.append(val) 

    def pop(self) -> None:
        top = self.top()

        if top == self.getMin():
            self.minStack.pop()
        
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.minStack:
            return -inf

        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()