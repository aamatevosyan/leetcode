class Solution:
    def calculate(self, s: str) -> int:
        result, last_number, current_number, prev_op = 0, 0, 0, '+'

        for c in s + '#':
            if c == ' ':
                continue

            if c.isdigit():
                current_number = current_number * 10 + int(c)
                continue
            
            if prev_op in '+':
                result += last_number
                last_number = current_number
            elif prev_op == '-':
                result += last_number
                last_number = -current_number
            elif prev_op == '/':
                last_number = trunc(last_number / current_number)
            elif prev_op == '*':
                last_number *= current_number
            
            prev_op, current_number = c, 0
        
        result += last_number

        return result
        