from collections import deque

class MyQueue:

    def __init__(self):
        self.input = deque()
        self.output = deque()

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        return self.peek_pop(pop=True)

    def peek(self) -> int:
        return self.peek_pop(pop=False)

    def peek_pop(self, pop: bool = False) -> int:
        if self.output:
            return self.output.pop() if pop else self.output[-1]

        while self.input:
            self.output.append(self.input.pop())
        
        return self.output.pop() if pop else self.output[-1]


    def empty(self) -> bool:
        return not self.input and not self.output
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()