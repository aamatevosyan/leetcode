from collections import defaultdict
from heapq import heapify, heappop

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for _from, _to in tickets:
            graph[_from].append(_to)
        
        for _from in graph:
            heapify(graph[_from])

        ans = []

        def dfs(s: str):
            while graph[s]:
                dfs(heappop(graph[s]))
            ans.append(s)

        dfs('JFK')
        return ans[::-1]