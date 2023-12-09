class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)

        for num in nums[k:]:
            heappushpop(heap, num)

        return heap[0]
        