class Solution:
    def countCharacters(self, s):
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        return counts

    def findAnagrams(self, s: str, p: str) -> List[int]:
        counts = self.countCharacters(p)
        start, n = 0, len(p)
        results = []

        localCount = defaultdict(int)

        for end in range(len(s)):
            end_char = s[end]
            localCount[end_char] += 1
            
            if end - start + 1 == n:
                flag = False

                if len(localCount) == len(counts):
                    for k in counts:
                        if k not in localCount or localCount[k] != counts[k]:
                            flag = True
                            break
                
                    if not flag:
                        results.append(start)
                
                localCount[s[start]] -= 1
                if localCount[s[start]] == 0:
                    localCount.pop(s[start])
                start += 1
        
        return results