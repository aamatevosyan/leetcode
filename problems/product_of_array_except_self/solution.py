class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0
        
        prefix, curr = [], 1
        for num in nums:
            prefix.append(curr)
            curr *= num
        
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] *= curr
            curr *= nums[i]
        
        return prefix