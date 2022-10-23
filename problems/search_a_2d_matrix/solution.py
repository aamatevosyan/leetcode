class Solution:
    def searchColumn(self, matrix: List[List[int]], target: int) -> int:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (r - l) // 2 + l

            if matrix[m][0] <= target:
                l = m + 1
            else:
                r = m - 1
        
        if matrix[m][0] > target:
            m -= 1
        
        return m
    
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r - l) // 2 + l

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = self.searchColumn(matrix, target)
        print(i)
        
        return self.search(matrix[i], target) != -1