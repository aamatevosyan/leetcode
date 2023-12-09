class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def connected(self, u: int, v: int) -> bool:
        return self.find(u) == self.find(v)
    
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
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)

        for equation in equations:
            if "==" in equation:
                u, v = equation[0], equation[3]

                uf.union((ord(u) - ord('a')), (ord(v) - ord('a')))
        
        for equation in equations:
            if "!=" in equation:
                u, v = equation[0], equation[3]
                
                if uf.connected((ord(u) - ord('a')), (ord(v) - ord('a'))):
                    return False
        
        return True
        