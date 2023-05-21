from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, q, path = defaultdict(list), deque(), []

        for start, end in prerequisites:
            graph[end].append(start)

        indegree = [0] * numCourses
        for start, end in prerequisites:
            indegree[start] += 1    
                
        for i in range(numCourses):
            if indegree[i] == 0:
                q.appendleft(i)

        while q:
            course = q.popleft()
            path.append(course)

            for i in graph[course]:
                indegree[i] -= 1

                if indegree[i] == 0:
                    q.appendleft(i)
        
        return path if len(path) == numCourses else []
                
