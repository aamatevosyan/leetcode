from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseReqs = defaultdict(list)

        for a, b in prerequisites:
            courseReqs[b].append(a)
        
        indegree = [0] * numCourses

        for v in courseReqs:
            for u in courseReqs[v]:
                indegree[u] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        cnt = 0

        while q:
            v = q.popleft()
            indegree[v] -= 1
            cnt += 1

            for u in courseReqs[v]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    q.append(u)

        return cnt == numCourses 

