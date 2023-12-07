class Solution:
    def __init__(self):
        self.result = []
        self.path = []
        self.n = 0

    def backtrack(self, graph: List[List[int]], v: int):
        self.path.append(v)

        if v + 1 == self.n:
            self.result.append(self.path[:])
            self.path.pop()
            return

        for child in graph[v]:
            self.backtrack(graph, child)
        
        self.path.pop()
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.n = len(graph)
        self.backtrack(graph, 0)

        return self.result
        