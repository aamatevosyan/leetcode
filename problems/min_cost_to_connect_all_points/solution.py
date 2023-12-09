from heapq import heapify

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, u: int, v: int) -> bool:
        p1, p2 = self.find(u), self.find(v)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = self.parent[p1]
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = self.parent[p2]
        else:
            self.parent[p2] = self.parent[p1]
            self.rank[p1] += 1
        
        self.count -= 1

        return True

class Solution:
    def manhattan_distance(self, p1: List[int], p2: List[int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, mst, q = len(points), 0, []

        for i in range(n):
            for j in range(i + 1, n):
                q.append((self.manhattan_distance(points[i], points[j]), i, j))
        
        heapify(q)
        
        uf = UnionFind(n)

        while q and uf.count != 1:
            w, u, v = heappop(q)

            if not uf.union(u, v):
                continue
        
            mst += w
        
        return mst
            


        