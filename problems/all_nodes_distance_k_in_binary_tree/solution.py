from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getGraph(self, root: TreeNode) -> Dict[int, List[int]]:
        graph = defaultdict(list)
        q = deque([root])

        while q:
            node = q.popleft()

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)

                q.append(node.left)
            
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)

                q.append(node.right)
        
        return graph

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = self.getGraph(root)
        q = deque([target.val])
        visited = set([target.val])
        result = []

        while q and k != -1:
            _len = len(q)

            for _ in range(_len):
                node = q.popleft()

                if k == 0:
                    result.append(node)
                    continue
                
                for child in graph[node]:
                    if not child in visited:
                        visited.add(child)
                        q.append(child)
            
            k -= 1
        
        return result
        
