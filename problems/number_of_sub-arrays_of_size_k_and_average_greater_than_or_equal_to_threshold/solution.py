class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, window, res = 0, 0, 0
        threshold = k * threshold

        for r in range(len(arr)):
            window += arr[r]

            if r - l + 1 < k:
                continue
            
            if r - l + 1 > k:
                window -= arr[l]
                l += 1
            
            if window >= threshold:
                res += 1
        
        return res
            