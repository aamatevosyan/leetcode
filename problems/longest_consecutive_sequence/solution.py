from sortedcontainers import SortedSet

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        counts = SortedSet(nums)
        last_num, count, max_count = None, 0, 1

        for num in counts:
            if last_num is None or num - last_num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
            
            last_num = num

        return max(max_count, count)