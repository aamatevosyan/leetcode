class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_count = Counter(t)
        distinct_chars, l, min_substr = len(char_count), 0, s[:] + " "

        for r in range(len(s)):
            if s[r] in char_count:
                char_count[s[r]] -= 1

                if char_count[s[r]] == 0:
                    distinct_chars -= 1
            
            while distinct_chars == 0 and l < len(s):
                if r - l + 1 < len(min_substr):
                    min_substr = s[l: r + 1]
                
                if s[l] in char_count:
                    char_count[s[l]] += 1

                    if char_count[s[l]] == 1:
                        distinct_chars += 1
                
                l += 1
        
        if len(min_substr) > len(s):
            return ""
        
        return min_substr
        