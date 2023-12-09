class Solution:
    def merge_sort(self, nums: List[int], l: int, r: int):
        if l == r:
            return

        m = l + (r - l) // 2

        self.merge_sort(nums, l, m)
        self.merge_sort(nums, m + 1, r)

        self.merge(nums, l, m, r)
    
    def merge(self, nums: List[int], l: int, m: int, r: int):
        n1, n2 = m - l + 1, r - m

        L, R = nums[l : m + 1], nums[m + 1: r + 1]

        i, j, k = 0, 0, l

        while i < n1 and j < n2:
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
        
        while i < n1:
            nums[k] = L[i]
            i += 1
            k += 1
        
        while j < n2:
            nums[k] = R[j]
            j += 1
            k += 1


    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)

        return nums
        
        