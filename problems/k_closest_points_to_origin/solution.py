from queue import PriorityQueue

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = PriorityQueue()

        for x, y in points:
            priority = x * x + y * y
            q.put((-priority, (x, y)))

            if q.qsize() > k:
                q.get()

        result = []
        for i in range(k):
            _, point = q.get()
            result.append(point)
        
        return result