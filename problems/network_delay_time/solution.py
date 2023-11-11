from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        
        for u, v, w in times:
            graph[u - 1].append((v - 1, w))
        
        dist = [-1] * n
        min_heap = [(0, k - 1)]

        while min_heap:
            d, u = heappop(min_heap)

            if dist[u] != -1:
                continue
            
            dist[u] = d
            
            for v, w in graph[u]:
                if dist[v] != -1:
                    continue
                
                heappush(min_heap, (d + w, v))
        
        if min(dist) == -1:
            return -1
        
        return max(dist)
        