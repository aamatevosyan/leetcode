from heapq import heappop, heappush

class Solution:
    def manhattan_distance(self, p1: List[int], p2: List[int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, mst_weight = len(points), 0
        visited = [False] * n
        dists = [math.inf] * n
        min_heap = [(0, 0)]
        dists[0] = 0
        vertex_count = 0

        while min_heap and vertex_count != n:
            w, u = heappop(min_heap)


            if visited[u]:
                continue
            
            visited[u] = True
            mst_weight += w
            vertex_count += 1

            for v in range(n):
                if visited[v]:
                    continue
                
                dist = self.manhattan_distance(points[u], points[v])
                if dist < dists[v]:
                    heappush(min_heap, (dist, v))
                    dists[v] = dist

        return mst_weight
        
        
        