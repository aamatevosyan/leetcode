from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pattern_counts = Counter(t)
        counter, start, min_len, min_substring =  len(pattern_counts), 0, len(s) + 1, ""

        for end in range(len(s)):
            if s[end] in pattern_counts:
                pattern_counts[s[end]] -= 1

                if pattern_counts[s[end]] == 0:
                    counter -= 1
            
            while counter == 0:
                if min_len > end - start + 1:
                    min_len = end - start + 1
                    min_substring = s[start: end + 1]

                if s[start] in pattern_counts:
                    pattern_counts[s[start]] += 1
                
                    if pattern_counts[s[start]] == 1:
                        counter += 1
                    
                start += 1
        

        return min_substring
            

