class Solution:
    def canPartitionTarget(self, nums: List[int], target: int) -> bool:
        dp = [True] + [False] * target

        for i in range(len(nums)):
            for j in range(target, 0, -1):
                if j - nums[i] >= 0 and dp[j - nums[i]]:
                    dp[j] = True
        
        return dp[target]

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total & 1:
            return False
        
        return self.canPartitionTarget(nums, total >> 1)