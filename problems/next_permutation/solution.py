class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2

        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i < 0:
            self.reverse(nums, 0)
            return
        
        j = len(nums) - 1

        while nums[j] <= nums[i]:
            j -= 1
            
        nums[i], nums[j] = nums[j], nums[i]

        self.reverse(nums, i + 1)
    
    def reverse(self, nums: List[int], i: int) -> None:
        j = len(nums) - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1