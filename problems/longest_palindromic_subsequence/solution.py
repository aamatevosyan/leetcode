class Solution:
    @lru_cache(None)
    def helper(self, i: int, j: int, s: str) -> int:
        if i == j:
            return 1
        
        if i > j:
            return 0
        
        if s[i] == s[j]:
            return self.helper(i + 1, j - 1, s) + 2
        
        return max(
            self.helper(i + 1, j, s),
            self.helper(i, j - 1, s),
        )

    def longestPalindromeSubseq(self, s: str) -> int:
        return self.helper(0, len(s) - 1, s)