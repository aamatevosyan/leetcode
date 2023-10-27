from collections import deque

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0

        for to_push in pushed:
            pushed[i] = to_push
            i += 1

            while i > 0 and pushed[i - 1] == popped[j]:
                j += 1
                i -= 1       
        
        return i == 0
                

        