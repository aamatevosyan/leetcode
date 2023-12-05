from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window, need = defaultdict(int), defaultdict(int)
        
        for c in p:
            need[c] += 1

        result, l, valid = [], 0, 0

        for r, c in enumerate(s):
            if c in need:
                window[c] += 1
                
                if window[c] == need[c]:
                    valid += 1

            if r - l + 1 == len(p):
                if valid == len(need):
                    result.append(l)
                
                d = s[l]
                l += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        return result

        
        