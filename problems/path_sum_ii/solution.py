# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calcSum(self, root: Optional[TreeNode], currentElements: List[int], currentSum: int, targetSum: int, results: List[List[int]]):
        if not root:
            return

        currentSum += root.val

        currentElements.append(root.val)
        
        if not root.left and not root.right and currentSum == targetSum:
             results.append(currentElements.copy())
        else:
            if root.left:
                self.calcSum(root.left, currentElements, currentSum, targetSum, results)
            if root.right:
                self.calcSum(root.right, currentElements, currentSum, targetSum, results)

        currentElements.pop()

        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        currentSum = 0
        currentElements = []
        results = []

        self.calcSum(root, currentElements, currentSum, targetSum, results)

        return results