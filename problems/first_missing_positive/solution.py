class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positives = set([num for num in nums if num > 0])

        for i in range(1, len(nums) + 2):
            if i not in positives:
                return i