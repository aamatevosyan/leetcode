class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        compressed_s = self.compress(s)

        return sum(self.check(compressed_s, self.compress(word)) for word in words)

    def compress(self, s: str) -> List[Tuple[str, int]]:
        groups, cnt, last_char = [], 0, s[0]
        for c in s:
            if c == last_char:
                cnt += 1
            else:
                groups.append((last_char, cnt))
                last_char = c
                cnt = 1
        
        groups.append((last_char, cnt))

        return groups
    
    def check(self, s: List[Tuple[str, int]], word: List[Tuple[str, int]]) -> bool:
        if len(s) != len(word):
            return False
        
        for one, two in zip(s, word):
            c_one, c_two = one[0], two[0]
            if c_one != c_two:
                return False
            
            n_one, n_two = one[1], two[1]
            
            if n_one == n_two:
                continue
            
            if n_one < max(3, n_two):
                return False
        
        return True