class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            remainer, n = n & 1, n >> 1
            count += remainer

        return count