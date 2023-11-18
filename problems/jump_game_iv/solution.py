from collections import defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        q = deque([0])
        
        graph = defaultdict(set)
        for i, num in enumerate(arr):
            graph[num].add(i)
        
        seen = [False] * n
        seen[0] = True
        d = -1

        while q:
            curr = deque()
            d += 1

            for i in q:
                childs = graph[arr[i]] if arr[i] in graph else set()

                if i - 1 >= 0:
                    childs.add(i - 1)
                
                if i + 1 < len(arr):
                    childs.add(i + 1)

                for j in childs:
                    if seen[j]:
                        continue
                    
                    if j == n - 1:
                        return d + 1
                    
                    curr.append(j)
                    seen[j] = True
                
                if arr[i] in graph:
                    graph.pop(arr[i])

            q = curr
        
        return 0