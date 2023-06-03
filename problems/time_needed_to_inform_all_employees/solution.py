from collections import deque, defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q = deque([(headID, 0)])
        graph = defaultdict(list)

        for i, parent in enumerate(manager):
            if i == headID:
                continue
            
            graph[parent].append(i)

        max_time = 0

        while q:
            node, time = q.popleft()

            for child in graph[node]:
                q.append((child, time + informTime[node]))
            
            max_time = max(max_time, time + informTime[node])

        return max_time
