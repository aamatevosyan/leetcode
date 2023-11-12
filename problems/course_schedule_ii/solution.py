from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        path, indegree, q = [], [0] * numCourses, deque([])

        for d, s in prerequisites:
            graph[s].append(d)
            indegree[d] += 1
        
        for v, degree in enumerate(indegree):
            if degree == 0:
                q.append(v)
        
        while q:
            u = q.popleft()
            path.append(u)

            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
    
        return [] if len(path) != numCourses else path
        