from bisect import bisect_right

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        r = bisect_right(arr, x, 0, n - k)
        l = r - 1

        for _ in range(k):
            if r >= n or (l >= 0 and x - arr[l] <= arr[r] - x):
                l -= 1
            else:
                r += 1

        return arr[l + 1 : r]
        