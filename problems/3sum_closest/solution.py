class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        minDiff, minSum = float("inf"), float("inf")

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                diff = nums[i] + nums[l] + nums[r]

                if diff == target:
                    return target
                elif diff < target:
                    l += 1
                else:
                    r -= 1
                
                if minDiff > abs(diff - target):
                    minDiff = abs(diff - target)
                    minSum = diff
        
        return minSum