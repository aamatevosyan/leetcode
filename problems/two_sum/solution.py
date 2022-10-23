class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}

        for i in range(len(nums)):
            numDict[nums[i]] = i

        for i in range(len(nums)):
            if (target - nums[i]) in numDict and i != numDict[target - nums[i]]:
                return [i, numDict[target - nums[i]]]