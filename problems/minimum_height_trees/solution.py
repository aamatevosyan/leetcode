from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
        
        connections = [set() for _ in range(n)]
        for start, end in edges:
            connections[start].add(end)
            connections[end].add(start)
        
        leaves = deque((i for i in range(n) if len(connections[i]) == 1))
        remaining_nodes = n

        while remaining_nodes > 2:
            n = len(leaves)
            remaining_nodes -= n
            
            for _ in range(n):
                leaf = leaves.pop()

                connection = connections[leaf].pop()

                connections[connection].remove(leaf)
                if len(connections[connection]) == 1:
                    leaves.appendleft(connection)
        
        return list(leaves)
        
