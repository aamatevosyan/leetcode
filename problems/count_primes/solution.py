class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True] * n

        for i in range(2, int(n ** 0.5) + 1):
            if not prime[i]:
                continue
            
            for j in range(i * i, n, i):
                prime[j] = False
        
        cnt = 0
        for i in range(2, n):
            if prime[i]:
                cnt += 1
        
        return cnt
        