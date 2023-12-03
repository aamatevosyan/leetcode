class Solution:
    def __init__(self):
        self.result = []
        self.used = []
        self.path = []

    def backtrack(self, nums: List[int]) -> None:
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return
        
        for i, num in enumerate(nums):
            if self.used[i]:
                continue
            
            if i > 0 and nums[i] == nums[i - 1] and self.used[i - 1]:
                continue
            
            self.used[i] = True
            self.path.append(num)

            self.backtrack(nums)

            self.used[i] = False
            self.path.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.used = [False] * len(nums)
        nums.sort()

        self.backtrack(nums)

        return self.result
        