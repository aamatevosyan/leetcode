from heapq import heappop, heappush

class NumPair:
    def __init__(self, num, count):
        self.num = num
        self.count = count

    def __lt__(self, other):
        return self.count > other.count

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = defaultdict(int)
        numHeap = []

        for num in nums:
            numCount[num] += 1

        for num in numCount:
            pair = NumPair(num, numCount[num])
            heappush(numHeap, pair)

        results = []

        for i in range(k):
            results.append(heappop(numHeap).num)

        return results