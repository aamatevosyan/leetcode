class Solution:
    def __init__(self):
        self.result = []
        self.total = 0
        self.path = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtrack(candidates, target, 0)

        return self.result
    
    def backtrack(self, candidates: List[int], target: int, start: int) -> None:
        if self.total == target:
            self.result.append(self.path[:])

        if self.total >= target:
            return    

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            self.path.append(candidates[i])
            self.total += candidates[i]

            self.backtrack(candidates, target, i + 1)

            self.total -= candidates[i]
            self.path.pop()
        