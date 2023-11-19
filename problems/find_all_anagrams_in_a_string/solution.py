class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern_count = Counter(p)
        window_count = Counter()

        result, l = [], 0

        for r in range(len(s)):
            window_count[s[r]] += 1

            if r - l + 1 == len(p):
                if window_count == pattern_count:
                    result.append(l)
                
                window_count[s[l]] -= 1
                if window_count[s[l]] == 0:
                    window_count.pop(s[l])
                
                l += 1
        
        return result

        
        