from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []

        for row in matrix:
            for column in row:
                nums.append(column)
        
        ind = bisect_left(nums, target)
        return ind < len(nums) and nums[ind] == target