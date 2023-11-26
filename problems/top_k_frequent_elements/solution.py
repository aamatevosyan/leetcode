from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = list(Counter(nums).items())
        
        q = [(cnt, num) for num, cnt in num_count[:k]]
        heapify(q)

        for num, cnt in num_count[k:]:
            heappushpop(q, (cnt, num))
        
        return [num for _, num in q]
        