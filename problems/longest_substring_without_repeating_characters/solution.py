class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, length, char_ind = 0, 0, [-1] * 128

        for r in range(len(s)):
            n = ord(s[r])

            if char_ind[n] >= l:
                l = char_ind[n] + 1

            length = max(length, r - l + 1)
            char_ind[n] = r
        
        return length
        