class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        start, end = 0, 1

        intervals.sort(key=lambda x: x[start])

        cur_start, cur_end = intervals[0][start], intervals[0][end]

        merged = []
        for i in range(1, len(intervals)):
            interval = intervals[i]

            if interval[start] <= cur_end:
                cur_end = max(cur_end, interval[end])
            else:
                merged.append([cur_start, cur_end])
                cur_start = interval[start]
                cur_end = interval[end]
        
        merged.append([cur_start, cur_end])

        return merged 