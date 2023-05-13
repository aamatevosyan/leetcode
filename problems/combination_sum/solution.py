

class Solution:
    def premutate(
        self, 
        candidates: List[int], 
        combinations: List[int],
        result: List[List[int]], 
        target: int,
        current: int,
        index: int,
    ):
        if current == target:
            result.append(combinations[:])
        
        if current >= target:
            return
        
        for i in range(index, len(candidates)):
            combinations.append(candidates[i])

            self.premutate(candidates, combinations, result, target, current + candidates[i], i)

            combinations.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations, result = [], []

        self.premutate(candidates, combinations, result, target, 0, 0)

        return result