class Solution:
    def getPalindrome(self, s: str, l: int, r: int) -> Tuple[int, int] | None:
        if r >= len(s) or s[l] != s[r]:
            return None

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        return (l + 1, r - 1)

    def longestPalindrome(self, s: str) -> str:
        maxLen, _l, _r = 0, 0, 0

        for i in range(len(s)):
            palindromIndexes = [
                self.getPalindrome(s, i, i + 1),
                self.getPalindrome(s, i, i),
            ]

            for palindromIndex in palindromIndexes:
                if not palindromIndex:
                    continue
                
                l, r = palindromIndex

                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    _l, _r = l, r
        
        return s[_l : _r + 1]


            