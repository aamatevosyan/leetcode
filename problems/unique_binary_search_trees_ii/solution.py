# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generate(self, l: int, r: int):
        if l > r:
            return [None]
        
        generated = []

        for i in range(l, r + 1):
            left_generated = self.generate(l, i - 1)
            right_generated = self.generate(i + 1, r)

            for left in left_generated:
                for right in right_generated:
                    generated.append(
                        TreeNode(
                            i, 
                            left, 
                            right
                        )
                    )

        return generated

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if not n:
            return []
        
        return self.generate(1, n)
        