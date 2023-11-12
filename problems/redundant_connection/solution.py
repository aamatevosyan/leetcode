class UnionFind:
    def __init__(self, n: int):
        self.rank = [0] * (n + 1)
        self.parents = list(range(n + 1))
    
    def find(self, node: int) -> int:
        parent = self.parents[node]

        while parent !=  self.parents[parent]:
            self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        
        return parent
    
    def union(self, node1: int, node2: int) -> bool:
        parent1, parent2 = self.find(node1), self.find(node2)
        
        if parent1 == parent2:
            return False

        if self.rank[parent1] > self.rank[parent2]:
            self.parents[parent2] = parent1
        elif self.rank[parent1] < self.rank[parent2]:
            self.parents[parent1] = parent2
        else:
            self.parents[parent1] = parent2
            self.rank[parent2] += 1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind(len(edges))

        for u, v in edges:
            if union_find.union(u, v) is False:
                return [u, v]

