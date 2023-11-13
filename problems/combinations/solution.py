class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.helper(0, [], res, n, k)
        
        return res
    
    def helper(self, i: int, path: List[int], res: List[int], n: int, k: int) -> None:
        if len(path) == k:
            res.append(path)
            return

        if i > n:
            return
        
        for j in range(i + 1, n + 1):
            self.helper(j, path + [j], res, n, k)