from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = [-cnt for _, cnt in Counter(tasks).items()]
        heapify(q)
        
        totalTime = 0

        while True:
            remain = []
            cycle = n + 1

            while cycle > 0 and q:
                cnt = -1 * heappop(q)
                
                if cnt > 1:
                    remain.append(cnt - 1)
                cycle -= 1
                totalTime += 1
            
            for cnt in remain:
                heappush(q, -cnt)
            
            if not q:
                break
            
            totalTime += cycle
        
        return totalTime
        
