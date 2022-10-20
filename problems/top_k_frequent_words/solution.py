from heapq import heappop, heappush

class WordPair:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, other):
        if self.count != other.count:
            return self.count > other.count
        
        return self.word < other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordCount = defaultdict(int)
        wordHeap = []

        for word in words:
            wordCount[word] += 1

        for word in wordCount:
            heappush(wordHeap, WordPair(word, wordCount[word]))
        
        results = []

        for i in range(k):
            results.append(heappop(wordHeap).word)
        
        return results