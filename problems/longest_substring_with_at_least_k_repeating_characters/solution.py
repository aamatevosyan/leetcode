from collections import Counter

class Solution:
    @lru_cache(None)
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        char_count = Counter(s)    

        for i, c in enumerate(s):
            if char_count[c] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i + 1:], k)

                return max(left, right)
        
        return len(s)
        