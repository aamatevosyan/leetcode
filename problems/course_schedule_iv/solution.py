class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        ancestors = [set() for _ in range(numCourses)]
        indegree, q = [0] * numCourses, deque([])

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
                
                ancestors[v].add(u)
                ancestors[v].update(ancestors[u])

                if indegree[v] == 0:
                    q.append(v)
        
        return [d in ancestors[s] for s, d in queries]
        