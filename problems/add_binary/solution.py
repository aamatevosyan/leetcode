class Solution:
    def addBinary(self, a: str, b: str) -> str:
        base, carry, i, j = 2, 0, len(a) - 1, len(b) - 1
        answer = []

        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            
            if j >= 0:
                carry += int(b[j])
                j -= 1
            
            answer.append(str(carry % base))
            carry = carry // base
        
        return ''.join(reversed(answer))
        
        
        