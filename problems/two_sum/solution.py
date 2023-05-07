from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indexes = {}

        for i, num in enumerate(nums):
            num_indexes[num] = i

        for i, num in enumerate(nums):
            to_search = target - num

            if to_search in num_indexes and i != num_indexes[to_search]:
                return [i, num_indexes[to_search]]