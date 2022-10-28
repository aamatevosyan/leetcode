class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ind, i, j = m + n - 1, m - 1, n - 1

        while ind >= 0:
            if j < 0 or (i >= 0 and nums1[i] >= nums2[j]):
                nums1[ind] = nums1[i]
                i -= 1
            else:
                nums1[ind] = nums2[j]
                j -= 1
            
            ind -= 1
        