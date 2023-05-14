class Solution:
    def helper(self, nums: List[int], ind: int, subset: List[int], result: List[List[int]]):
        result.append(subset[:])

        if len(subset) == len(nums):
            return

        for i in range(ind, len(nums)):
            subset.append(nums[i])
            self.helper(nums, i + 1, subset, result)
            subset.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        self.helper(nums, 0, [], result)

        return result