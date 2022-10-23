class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (r - l) // 2 + l

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        if nums[-1] >= target:
            l, r = l, len(nums) - 1
        else:
            l, r = 0, l
        
        while l <= r:
            m = (r - l) // 2 + l

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1