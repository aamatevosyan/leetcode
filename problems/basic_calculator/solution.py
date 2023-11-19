class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign, st = 0, 0, 1, deque([1])

        for c in s:
            if c == " ":
                continue
            
            if c == "(":
                st.append(sign)
            elif c == ")":
                st.pop()
            elif c in ("+", "-"):
                res += sign * num
                sign = (1 if c == "+" else -1) * st[-1]
                num = 0
            else:
                num *= 10
                num += int(c)
        
        res += sign * num
        
        return res
        