class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = deque([start])
        seen = [False] * n

        while q:
            i = q.popleft()

            if seen[i]:
                continue
            
            if arr[i] == 0:
                return True
            
            seen[i] = True
            
            if i + arr[i] < n:
                q.append(i + arr[i])
            
            if i - arr[i] >= 0:
                q.append(i - arr[i])
        
        return False