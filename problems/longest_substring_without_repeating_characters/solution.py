class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, max_len, char_ind = 0, 0, {}

        for r in range(len(s)):
            if s[r] in char_ind and l <= char_ind[s[r]]:
                l = char_ind[s[r]] + 1
            
            max_len = max(r - l + 1, max_len)
            char_ind[s[r]] = r
        
        return max_len
        