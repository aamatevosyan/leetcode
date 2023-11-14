class Solution:
    def canParitionTarget(self, nums: List[int], target: int):
        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(len(nums)):
            curr = [False] * (target + 1)

            for j in range(1, target + 1):
                exclude = dp[j]
                include = False
                
                if j - nums[i] >= 0:
                    include = dp[j - nums[i]]

                curr[j] = exclude or include

            dp = curr
        
        return curr[target]

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total & 1:
            return False
        
        return self.canParitionTarget(nums, total >> 1)
        