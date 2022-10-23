from collections import defaultdict

class Solution:
    def countCharacters(self, s):
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        return counts

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        one, two = self.countCharacters(s), self.countCharacters(t)

        if len(one) != len(two):
            return False
        
        for k in one:
            if one[k] != two[k]:
                return False
        
        return True