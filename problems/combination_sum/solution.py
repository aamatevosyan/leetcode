class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        self.helper(0, candidates, [], res, target)
        
        return res
    
    def helper(self, i: int, candidates: List[int], path: List[int], res: List[int], left: int) -> None:
        if left == 0:
            res.append(path)
            return

        if left < 0:
            return
        
        for j in range(i, len(candidates)):
            self.helper(j, candidates, path + candidates[j:j+1], res, left - candidates[j])