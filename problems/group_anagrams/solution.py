from collections import Counter

class Solution:
    def countCharacters(self, s: str) -> str:
        charCounts = Counter(s)
        
        result = ''
        for key, count in sorted(charCounts.items()):
            result += key * count
        
        return result

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams, groups = {}, []

        for s in strs:
            normalized = self.countCharacters(s)
            
            if not normalized in anagrams:
                groups.append([])
                anagrams[normalized] = len(groups) - 1
            
            groups[anagrams[normalized]].append(s)


        return groups