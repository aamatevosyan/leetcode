class Solution:
    def mapToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'IV': 4,
            'X': 10,
            'IX': 9,

            'L': 50,
            'XL': 40,
            'C': 100,
            'XC': 90,

            'D': 500,
            'CD': 400,
            'M': 1000,
            'CM': 900,
        }

        return mapping[s]
    
    def isLowering(self, l: str, s: str) -> bool:
        combined = l + s

        return combined in (
            'IV',
            'IX',
            'XL',
            'XC',
            'CD',
            'CM'
        )


    def romanToInt(self, s: str) -> int:
        i = 0
        carry = 0

        while i < len(s):
            c = s[i]
            
            if i + 1 < len(s) and self.isLowering(c, s[i + 1]):
                carry += self.mapToInt(c + s[i + 1])
                i += 2
            else:
                carry += self.mapToInt(c)
                i += 1

        return carry