class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 != 0:
            return False
        
        _sum, target = target, target // 2

        dp = [False] * (_sum + 1)
        dp[0] = True

        currSum = 0

        for num in nums:
            currSum += num
            for val in range(min(currSum, target) - num, -1, -1):
                if dp[val]:
                    dp[val + num] = True

            if dp[target]:
                 return True
        
        return False
