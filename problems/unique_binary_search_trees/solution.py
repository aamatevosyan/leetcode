class Solution:
    @lru_cache()
    def count(self, l: int, r: int) -> int:
        if l > r:
            return 1
        
        cnt = 0

        for i in range(l, r + 1):
            left = self.count(l, i - 1)
            right = self.count(i + 1, r)

            cnt += left * right
        
        return cnt

    def numTrees(self, n: int) -> int:
        return self.count(1, n)
        