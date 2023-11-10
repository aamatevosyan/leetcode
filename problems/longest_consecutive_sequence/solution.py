class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct_nums = sorted(set(nums))
        max_count, cnt, last_num = 0, 0, None

        for num in distinct_nums:
            if last_num is None or num - last_num == 1:
                cnt += 1
            else:
                max_count = max(max_count, cnt)
                cnt = 1
            
            last_num = num

        return max(max_count, cnt)
        