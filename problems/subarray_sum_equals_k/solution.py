class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_count, prefix_sum, cnt = { 0: 1 }, 0, 0
        
        for num in nums:
            prefix_sum += num

            if (prefix_sum - k) in num_count:
                 cnt += num_count[prefix_sum - k]

            if prefix_sum not in num_count:
                num_count[prefix_sum] = 1
            else:
                num_count[prefix_sum] += 1
        
        return cnt