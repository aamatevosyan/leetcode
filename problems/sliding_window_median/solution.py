from heapq import heappop, heappush
import heapq

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        minHeap, maxHeap, n = [], [], len(nums)
        result = [0.0 for _ in range(n - k + 1)]

        for (i, num) in enumerate(nums):
            if not maxHeap or -maxHeap[0] >= num:
                heappush(maxHeap, -num)
            else:
                heappush(minHeap, num)

            if len(maxHeap) > len(minHeap) + 1:
                heappush(minHeap, -heappop(maxHeap))
            elif len(maxHeap) < len(minHeap):
                heappush(maxHeap, -heappop(minHeap))
            
            if i - k + 1 >= 0:
                if len(maxHeap) == len(minHeap):
                    result[i - k + 1] = -maxHeap[0] / 2.0 + minHeap[0] / 2.0
                else:
                    result[i - k + 1] = -maxHeap[0] / 1.0

                elementToBeRemoved = nums[i - k + 1]
                if elementToBeRemoved <= -maxHeap[0]:
                    elementToBeRemoved = -elementToBeRemoved
                    heap = maxHeap
                else:
                    heap = minHeap
                
                ind = heap.index(elementToBeRemoved)
                heap[ind] = heap[-1]
                heap.pop()

                if ind < len(heap):
                    heapq._siftup(heap, ind)
                    heapq._siftdown(heap, 0, ind)
                
                if len(maxHeap) > len(minHeap) + 1:
                    heappush(minHeap, -heappop(maxHeap))
                elif len(maxHeap) < len(minHeap):
                    heappush(maxHeap, -heappop(minHeap))
            


        return result
