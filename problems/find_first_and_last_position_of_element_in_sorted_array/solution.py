class Solution:
    def left_bound(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return l if l < len(nums) and nums[l] == target else -1

    def right_bound(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return r if r >= 0 and nums[r] == target else -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        min_l = self.left_bound(nums, target)
        
        if min_l == -1:
            return [-1, -1]
        
        max_r = self.right_bound(nums, target)
        
        return [min_l, max_r]

        