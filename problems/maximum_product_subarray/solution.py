class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxProduct, prevMax, prevMin = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            options = (prevMax * nums[i], prevMin * nums[i], nums[i])
            currMin, currMax = min(*options), max(*options)
            
            maxProduct = max(maxProduct, currMax)
            prevMax, prevMin = currMax, currMin
        
        return maxProduct