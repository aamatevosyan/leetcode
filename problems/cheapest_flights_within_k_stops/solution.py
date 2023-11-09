from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph, q = [[] for _ in range(n)], [(0, src, k + 1)]
        prices = [[math.inf] * (k + 2) for _ in range(n)]

        for u, v, w in flights:
            graph[u].append((v, w))
        
        while q:
            cost, u, stops = heappop(q)
            
            if u == dst:
                return cost
                        
            if stops <= 0:
                continue
            
            for v, w in graph[u]:
                new_cost = cost + w
                if new_cost < prices[v][stops - 1]:
                    prices[v][stops - 1] = new_cost
                    heappush(q, (new_cost, v, stops - 1))  

        return -1
            
        