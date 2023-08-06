class Solution:
    def factors(self, n: int):
        i = 1
        while i <= n:
            if n % i == 0:
                yield i
            
            i += 1

    def kthFactor(self, n: int, k: int) -> int:
        cnt = 0
        
        for num in self.factors(n):
            if num > n:
                break
            
            if cnt + 1 == k:
                return num
            
            cnt += 1

        return -1 