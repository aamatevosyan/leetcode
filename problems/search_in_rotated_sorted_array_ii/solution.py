class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r - l) // 2 + l

            if nums[m] == target:
                return True

            if nums[l] == nums[m] and nums[r] == nums[m]:
                l += 1
                r -= 1
            elif nums[l] <= nums[m]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target <= nums[r] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

        return False