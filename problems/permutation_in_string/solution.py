class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, valid, need, window = 0, 0, defaultdict(int), defaultdict(int)

        for c in s1:
            need[c] += 1
        
        for r, c in enumerate(s2):
            if c in need:
                window[c] += 1

                if window[c] == need[c]:
                    valid += 1
            
            if r - l + 1 >= len(s1):
                if valid == len(need):
                    return True
                
                d = s2[l]
                l += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1

                    window[d] -= 1 
        
        return False

        