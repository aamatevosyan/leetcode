# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr = root
        self.stack = []

    def next(self) -> int:
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left
        else:
            self.curr = self.stack.pop()
            curr = self.curr
            self.curr = self.curr.right
            
        return curr.val

    def hasNext(self) -> bool:
        return self.stack or self.curr 


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()