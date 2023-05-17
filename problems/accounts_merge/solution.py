from collections import defaultdict
from sortedcontainers import SortedSet

class Solution:
    def dfs(self, accounts: List[List[str]], graph: Dict[str, List[int]], visited: Set[str], result: Set[str], i: int):
        if visited[i]:
            return

        visited[i] = True
        _, *emails = accounts[i]

        for email in emails:
            result.add(email)

            for ind in graph[email]:
                self.dfs(accounts, graph, visited, result, ind) 


    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = [False] * len(accounts)
        graph = defaultdict(list)
        result = []

        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                graph[email].append(i)
        
        for i, account in enumerate(accounts):
            if visited[i]:
                continue
            
            name, emails = account[0], SortedSet()
            self.dfs(accounts, graph, visited, emails, i) 
            
            result.append([name, *emails])

        
        return result