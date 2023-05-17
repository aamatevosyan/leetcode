WHITESPACE, PLUS, MINUS, ZERO = ' ', '+', '-', '0'
MIN, MAX = -1 * (2 ** 31), (2 ** 31) - 1

class Solution:
    def myAtoi(self, s: str) -> int:
        i, result = 0, 0

        while i < len(s) and s[i] == WHITESPACE:
            i += 1
        
        sign = 1
        if i < len(s) and s[i] in [PLUS, MINUS]:
            if s[i] == MINUS:
                sign = -1
            i += 1
        
        while i < len(s) and s[i] == ZERO:
            i += 1
        
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        result = sign * result
        
        if result < MIN:
            result = MIN
        elif result > MAX:
            result = MAX
        
        return result