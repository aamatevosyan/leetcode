class Solution:
    def expand(self, s: str, i: int, j: int) -> Tuple[int, int, int]:
        l, r = i, j

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return r - j

    def countSubstrings(self, s: str) -> int:
        return sum(
            (self.expand(s, i, i) for i in range(len(s)))
        ) + sum(
            (self.expand(s, i, i + 1) for i in range(len(s)))
        )
        
        