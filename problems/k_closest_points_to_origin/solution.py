from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = [ (-(x * x + y * y), x, y) for x, y in points[:k]]
        heapify(q)

        for x, y in points[k:]:
            dist = x * x + y * y
            heappushpop(q, (-dist, x, y))
        
        return [(x, y) for _, x, y in q]