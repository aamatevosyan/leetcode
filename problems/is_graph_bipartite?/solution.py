class Solution:
    def __init__(self):
        self.color = []
        self.visited = []
        self.graph = []
        self.is_bipartite = True

    def traverse(self, v: int):
        if not self.is_bipartite:
            return
        
        self.visited[v] = True
        
        for w in self.graph[v]:
            if not self.visited[w]:
                self.color[w] = not self.color[v]

                self.traverse(w)
            else:
                if self.color[w] == self.color[v]:
                    self.is_bipartite = False
                    return

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        
        self.visited = [False] * n
        self.color = [False] * n
        self.graph = graph

        for v in range(n):
            if not self.visited[v]:
                self.traverse(v)

                if not self.is_bipartite:
                    return False

        return True
        