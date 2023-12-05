class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, max_len, char_ind = 0, 0, {}

        for r, c in enumerate(s):
            if c in char_ind and l <= char_ind[c]:
                l = char_ind[c] + 1
            
            max_len = max(r - l + 1, max_len)
            char_ind[c] = r
        
        return max_len
        