from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapper, result, _sum = defaultdict(int), 0, 0
        mapper[0] = 1

        for num in nums:
            _sum += num

            if _sum - k in mapper:
                result += mapper[_sum - k]
            
            mapper[_sum] += 1

        return result