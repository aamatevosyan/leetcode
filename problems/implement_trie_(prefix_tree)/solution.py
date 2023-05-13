LETTER_COUNT = 26
LOWEST_ORD = ord('a')

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.mapping = [-1] * LETTER_COUNT

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            a = ord(c) - LOWEST_ORD
            if curr.mapping[a] == -1:
                curr.mapping[a] = TrieNode()

            curr = curr.mapping[a]
        
        curr.isWord = True
        
    def _search(self, word: str) -> TrieNode:
        curr = self.root

        for c in word:
            a = ord(c) - LOWEST_ORD
            if curr.mapping[a] == -1:
                return None
                
            curr = curr.mapping[a]
        
        if curr == self.root:
            return None

        return curr

    def search(self, word: str) -> bool:
        node = self._search(word)

        return node and node.isWord
        

    def startsWith(self, prefix: str) -> bool:
        node = self._search(prefix)

        return node is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)