from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getPathSum(self, root: Optional[TreeNode], currentSum: int, targetSum: int, preSum: Dict[int, int]) -> int:
        if not root:
            return 0
        
        currentSum += root.val
        cnt = preSum[currentSum - targetSum]

        preSum[currentSum] += 1
        cnt += self.getPathSum(root.left, currentSum, targetSum, preSum)
        cnt += self.getPathSum(root.right, currentSum, targetSum, preSum)
        preSum[currentSum] -= 1

        return cnt

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pre_sum = defaultdict(int)
        pre_sum[0] = 1

        return self.getPathSum(root, 0, targetSum, pre_sum)

        