from bisect import bisect_left
from random import randint

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.nums = w[:]
        self.sum = sum(w)
        
        for i in range(1, len(w)):
            self.nums[i] += self.nums[i - 1]
        

    def pickIndex(self) -> int:
        num = randint(1, self.sum)
        ind = bisect_left(self.nums, num)

        return ind


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()