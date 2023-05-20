class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prev, curr = 0, nums[0]

        for i in range(1, len(nums)):
            prev, curr = curr, max(curr, prev + nums[i])

        return curr