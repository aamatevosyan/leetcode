class Solution:
    def rob_straight(self, nums: List[int]) -> int:
        prev_no_rob, prev_robbed = 0, 0

        for num in nums:
            max_no_rob = max(prev_no_rob, prev_robbed)

            prev_robbed = prev_no_rob + num
            prev_no_rob = max_no_rob
        
        return max(prev_no_rob, prev_robbed)

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        
        return max(
            self.rob_straight(nums[1:]),
            self.rob_straight(nums[:-1]),
        )

        