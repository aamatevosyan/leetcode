class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        
        start, end = intervals[0]
        cnt = 0

        for _start, _end in intervals[1:]:
            if _start < end:
                cnt += 1
            else:
                end = _end
        
        return cnt