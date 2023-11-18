class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        max_ind = 0
            
        for i in range(0, n - 1):
            for j in range(max_ind + 1, min(i + nums[i] + 1, n)):
                dp[j] = dp[i] + 1

            max_ind = max(max_ind, i + nums[i])

        return dp[-1]

            
        