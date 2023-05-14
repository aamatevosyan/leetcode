class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l, m, r = 0, 0, len(nums) - 1

        while m <= r:
            if nums[m] == 1:
                m += 1
            elif nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            else:
                nums[r], nums[m] = nums[m], nums[r]
                r -= 1


        