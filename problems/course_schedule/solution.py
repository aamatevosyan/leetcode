class Solution:
    def dfs(self, src: int, visited: List[int], graph: List[List[int]]):
        if visited[src] == 1:
            return True
        
        if visited[src] == -1:
            return False
        
        visited[src] = -1

        for v in graph[src]:
            if not self.dfs(v, visited, graph):
                return False
        
        visited[src] = 1

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for d, s in prerequisites:
            graph[s].append(d)
        
        for v in range(numCourses):
            if not self.dfs(v, visited, graph):
                return False
        
        return True
        