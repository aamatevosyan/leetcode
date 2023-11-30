class Solution:
    def helper(self, i: int, nums: List[int], curr_set: List[int], result: List[int]) -> None:
        if (i == len(nums)):
            result.append(curr_set[:])
            return
        
        curr_set.append(nums[i])
        self.helper(i + 1, nums, curr_set, result)
        curr_set.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        self.helper(i + 1, nums, curr_set, result)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        
        self.helper(0, nums, [], result)

        return result
        