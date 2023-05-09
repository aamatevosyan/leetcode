class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        q = []

        while n:
            remainer, n = n & 1, n >> 1
            q.append(remainer)
        
        for i in range(32 - len(q)):
            q.append(0)
        
        for el in q:
            ans = ans << 1
            ans += el
        
        return ans