from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        characterCounts, bonus, count = defaultdict(int), 0, 0

        for c in s:
            characterCounts[c] += 1
        
        for c in characterCounts:
            charCount = characterCounts[c]

            if bonus == 0 and charCount % 2 == 1:
                bonus = 1
            
            count += charCount // 2
        
        return count * 2 + bonus


