class Solution:
    def countCharacters(self, s):
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        result = ''
        for key, count in sorted(counts.items()):
            for i in range(count):
                result += key
        
        return result

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        groups = []

        for s in strs:
            c = self.countCharacters(s)
            
            if not c in anagrams_dict:
                groups.append([])
                anagrams_dict[c] = len(groups) - 1
            
            groups[anagrams_dict[c]].append(s)


        return groups