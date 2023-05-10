class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums) - 2):
            l, r, t = i + 1, len(nums) - 1, nums[i]

            while l < r:
                if nums[l] + nums[r] + t > 0:
                    r -= 1
                elif nums[l] + nums[r] + t < 0:
                    l += 1
                else:
                    result.add((nums[l], nums[r], t))

                    while l < r and nums[l] == nums[l + 1]: l += 1
                    while l < r and nums[r] == nums[r - 1]: r -= 1
                    l += 1
                    r -= 1
        
        return list(result)
