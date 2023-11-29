class Solution:
    def expand(self, s: str, i: int, j: int) -> Tuple[int, int, int]:
        l, r = i, j

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return (r - l - 1, l + 1, r - 1)


    def longestPalindrome(self, s: str) -> str:
        l, r, max_len = 0, 0, 0

        for i in range(len(s)):
            max_len, l, r = max(
                (max_len, l, r),
                self.expand(s, i, i),
                self.expand(s, i, i + 1),
            )

        return s[l : r + 1]
        