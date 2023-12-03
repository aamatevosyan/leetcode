class Solution:
    def __init__(self):
        self.result = []
        self.total = 0
        self.path = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtrack(candidates, target, 0)

        return self.result
    
    def backtrack(self, candidates: List[int], target: int, start: int) -> None:
        if self.total == target:
            self.result.append(self.path[:])

        if self.total >= target:
            return    

        for i in range(start, len(candidates)):
            self.path.append(candidates[i])
            self.total += candidates[i]

            self.backtrack(candidates, target, i)

            self.total -= candidates[i]
            self.path.pop()