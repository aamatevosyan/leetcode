from collections import Counter

class Solution:
    def partitionString(self, s: str) -> int:
        last_seen, cnt, start_index = [-1] * 26, 1, 0

        for i in range(len(s)):
            char_num = ord(s[i]) - ord('a')

            if last_seen[char_num] >= start_index:
                cnt += 1
                start_index = i
            
            last_seen[char_num] = i

        return cnt