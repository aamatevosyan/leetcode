from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagramCharCounts = Counter(p)
        l, n = 0, len(p)
        results = []

        windowCharCounts = defaultdict(int)

        for r in range(len(s)):
            c = s[r]
            windowCharCounts[c] += 1
            
            if r - l + 1 == n:
                if windowCharCounts == anagramCharCounts:
                    results.append(l)
                
                t = s[l]
                windowCharCounts[t] -= 1

                if windowCharCounts[t] == 0:
                    windowCharCounts.pop(t)
                l += 1
        
        return results