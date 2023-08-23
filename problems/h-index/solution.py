from heapq import heappush, heapify

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        q = [-1 * citation for citation in citations]
        heapify(q)
        h_index = 0

        while q and h_index < -1 * heappop(q):
            h_index += 1

        return h_index