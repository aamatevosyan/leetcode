from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = defaultdict(int)
        for c in s1:
            s1Count[c] += 1

        localCount = defaultdict(int)

        start = 0
        for end in range(len(s2)):
            endChar = s2[end]
            localCount[endChar] += 1

            if end - start + 1 == len(s1):
                if localCount == s1Count:
                    return True

                localCount[s2[start]] -= 1

                if localCount[s2[start]] == 0:
                    localCount.pop(s2[start])

                start += 1