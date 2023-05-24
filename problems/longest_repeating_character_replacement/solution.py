from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_counts, start, max_len, max_count = defaultdict(int), 0, 0, 0

        for end in range(len(s)):
            character_counts[s[end]] += 1

            max_count = max(max_count, character_counts[s[end]])

            if end - start + 1 - max_count > k:
                character_counts[s[start]] -= 1
                start += 1

            max_len = end - start + 1

        return max_len



