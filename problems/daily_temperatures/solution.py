from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        remain = deque()

        for i in range(len(temperatures) - 1):
            remain.append(i)
            
            while remain and temperatures[remain[-1]] < temperatures[i + 1]:
                ind = remain.pop()
                result[ind] = i - ind + 1
        
        return result