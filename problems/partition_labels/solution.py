class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastCharIndex = {}

        for (i, c) in enumerate(s):
            lastCharIndex[c] = i
        
        partitions = []
        start, end = 0, 0

        for i in range(len(s)):
            c = s[i]
            end = max(end, lastCharIndex[c])

            if end == i:
                partitions.append(end - start + 1)
                start = end + 1

        return partitions
