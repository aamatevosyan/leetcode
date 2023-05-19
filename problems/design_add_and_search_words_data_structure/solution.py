LETTER_COUNT = 26
LOWEST_ORD = ord('a')
WILDCARD = ord('.') - LOWEST_ORD

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.mapping = [-1] * LETTER_COUNT

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            a = ord(c) - LOWEST_ORD
            if curr.mapping[a] == -1:
                curr.mapping[a] = TrieNode()

            curr = curr.mapping[a]
        
        curr.isWord = True

    def search(self, word: str) -> bool:
        candidates = [self.root]

        for i, c in enumerate(word):
            a = ord(c) - LOWEST_ORD

            newCandidates = []

            for curr in candidates:
                options = range(LETTER_COUNT) if a == WILDCARD else [a]
                
                for o in options:
                    if curr.mapping[o] == -1:
                        continue
                    
                    if i == len(word) - 1 and curr.mapping[o].isWord:
                        return True
                    
                    newCandidates.append(curr.mapping[o])
            
            if not newCandidates:
                return False
                
            candidates = newCandidates
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)