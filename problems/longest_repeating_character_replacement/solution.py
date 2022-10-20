from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characterCount = defaultdict(int)

        start = 0
        maxCharacterCount = 0
        maxLen = 0

        for end in range(len(s)):
            characterCount[s[end]] += 1
            maxCharacterCount = max(maxCharacterCount, characterCount[s[end]])

            if end - start + 1 > maxCharacterCount + k:
                characterCount[s[start]] -= 1
                start += 1

            maxLen = max(maxLen, end - start + 1)


        return maxLen