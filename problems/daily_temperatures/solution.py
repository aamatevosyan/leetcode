from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        remain = deque()

        for i in range(len(temperatures) - 1, -1, -1):
            while remain and temperatures[remain[-1]] <= temperatures[i]:
                remain.pop()
            
            result[i] = remain[-1] - i if remain else 0
            remain.append(i)
            
        
        return result