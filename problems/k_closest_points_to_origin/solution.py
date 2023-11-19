from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []

        for x, y in points:
            dist = x * x + y * y
            heappush(q, (-dist, x, y))

            if len(q) > k:
                heappop(q)
        
        return [(x, y) for _, x, y in q]