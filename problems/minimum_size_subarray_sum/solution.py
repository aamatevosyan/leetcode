class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = len(nums) + 1
        l, _sum = 0, 0

        for r in range(len(nums)):
            _sum += nums[r]

            while _sum >= target:
                min_len = min(min_len, r - l + 1)
                _sum -= nums[l]
                l += 1
        
        return min_len if min_len <= len(nums) else 0
