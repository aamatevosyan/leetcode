class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_no_robbed, prev_robbed = 0, 0

        for num in nums:
            max_money = max(prev_no_robbed, prev_robbed)

            prev_robbed = prev_no_robbed + num
            prev_no_robbed = max_money
        
        return max(prev_no_robbed, prev_robbed)
            
        