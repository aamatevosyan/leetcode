class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened, res = 0, ''
        
        for c in s:
            if c == '(':
                opened += 1
                if opened > 1:
                    res += '('
            else:
                opened -= 1
                if opened > 0:
                    res += ')'
            
        return res
            
            
            
        