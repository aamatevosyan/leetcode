MAX, MIN = 2 ** 31 - 1, - (2 ** 31)

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        n = 0

        while x % 10 == 0:
            x //= 10

        sign = 1 if x > 0 else -1
        n = x % 10 if x > 0 else (x % 10) - 10
        x //= 10 if x > 0 else -10

        while x != 0:
            digit = x % 10
            x //= 10

            if (
                n > (MAX // 10)
                or (n == (MAX // 10) and digit > 7)
                or n < (MIN // 10) + 1
                or (n == (MIN // 10) + 1 and digit < -8)
            ):
                return 0
            
            n = n * 10 + sign * digit
        
        return n
