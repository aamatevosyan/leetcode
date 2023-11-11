class Solution:
    def get_sums(self, nums: List[int], f, f_sum) -> int:
        curr_sum = 0

        for num in nums:
            curr_sum = f(curr_sum + num, num)
            f_sum = f(f_sum, curr_sum)
        
        return f_sum

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = self.get_sums(nums, max, -math.inf)

        if max_sum < 0:
            return max_sum

        min_sum = self.get_sums(nums, min, math.inf)
        total_sum = sum(nums)

        return max(max_sum, total_sum - min_sum)
        