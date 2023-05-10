class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_indexes = [-1] * 128
        window_start, window_length, longest_length = 0, 0, 0

        for i in range(len(s)):
            n = ord(s[i])
            if char_indexes[n] == -1:
                window_length += 1
            else:
                if char_indexes[n] > window_start:
                    window_start = char_indexes[n]
                window_length = i - window_start
            
            char_indexes[n] = i
            if longest_length < window_length:
                longest_length = window_length
            
        return longest_length