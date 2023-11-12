class Node:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = None
    
    @staticmethod
    def insert(node: Optional[Node], start: int, end: int) -> (Node, bool):
        if not node:
            return Node(start, end), True

        if node.start <= start < node.end or node.start < end <= node.end or (
            start < node.start and end > node.end
        ):
            return node, False
        
        if start < node.start:
            node.left, success = MyCalendar.insert(node.left, start, end)
        else:
            node.right, success = MyCalendar.insert(node.right, start, end)
        
        return node, success
        


    def book(self, start: int, end: int) -> bool:
        self.root, success = self.insert(self.root, start, end)

        return success
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)