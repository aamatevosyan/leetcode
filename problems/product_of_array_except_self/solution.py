class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        result = [1]

        for i in range(len(nums) - 1):
            result.append(result[i] * nums[i])
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * right
            right *= nums[i]
        
        return result