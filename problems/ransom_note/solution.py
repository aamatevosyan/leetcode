from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        magazineLetterCounts = defaultdict(int)

        for c in magazine:
            magazineLetterCounts[c] += 1

        for c in ransomNote:
            magazineLetterCounts[c] -= 1
            if magazineLetterCounts[c] < 0:
                return False
        
        return True
