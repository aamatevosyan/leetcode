class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0)

        return self.result
    
    def backtrack(self, nums: List[int], start: int) -> None:
        self.result.append(self.path[:])

        if len(nums) == start:
            return

        for i in range(start, len(nums)):
            self.path.append(nums[i])

            self.backtrack(nums, i + 1)
            
            self.path.pop()


        