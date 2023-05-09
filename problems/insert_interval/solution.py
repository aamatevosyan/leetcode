class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals):
            if intervals[i][0] > newInterval[0]:
                break
            i += 1
        
        result = []
        intervals = intervals[:i] + [newInterval] + intervals[i:]
        _start, _end = intervals[0]

        for start, end in intervals[1:]:
            if start <= _end:
                _end = max(end, _end)
            else:
                result.append((_start, _end))
                _start, _end = start, end
        
        result.append((_start, _end))

        return result

