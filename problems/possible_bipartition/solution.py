from collections import deque

class Solution:
    def bfs(self, graph: List[List[int]], visited: List[bool], color: List[bool], v: int):
        q = deque([v])
        visited[v] = True

        while q:
            u = q.popleft()

            for w in graph[u]:
                if not visited[w]:
                    color[w] = not color[u]
                    visited[w] = True
                    q.append(w)
                elif color[w] == color[u]:
                    return False
        
        return True


    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]

        for v, w in dislikes:
            graph[v - 1].append(w - 1)
            graph[w - 1].append(v - 1)

        visited, color = [False] * n, [False] * n

        for v in range(n):
            if graph[v] and not visited[v] and not self.bfs(graph, visited, color, v):
                return False
        
        return True