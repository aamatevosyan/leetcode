# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = (r - l) // 2 + l

            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        
        return l