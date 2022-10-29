from collections import Counter
from heapq import nlargest

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        wordCount = sorted(counter.items())
        results = [el[0] for el in nlargest(k, wordCount, key=lambda x: x[1])]
        
        return results