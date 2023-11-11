class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        
        for i in range(len(edges)):
            u, v = edges[i]
            w = succProb[i]

            graph[u].append((v, w))
            graph[v].append((u, w))
        
        dist = [0] * n
        min_heap = [(-1, start_node)]

        while min_heap:
            d, u = heappop(min_heap)

            if dist[u] != 0:
                continue
            
            dist[u] = d * -1
            
            for v, w in graph[u]:
                if dist[v] != 0:
                    continue
                
                heappush(min_heap, (d * w, v))
        
        return dist[end_node]
        