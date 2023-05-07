from collections import Counter

class Solution:
    def countCharacters(self, s):
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        return counts

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCounter = Counter(s)

        for el in t:
            if not el in sCounter:
                return False
            
            sCounter.update({ el: -1 })

            if sCounter[el] < 0:
                return False

        return True