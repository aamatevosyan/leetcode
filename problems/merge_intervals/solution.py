class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda x: x[0])
        _start, _end = intervals[0]

        merged = []

        for start, end in intervals[1:]:
            if start <= _end:
                _end = max(_end, end)
            else:
                merged.append([_start, _end])
                _start, _end = start, end
        
        merged.append([_start, _end])

        return merged 