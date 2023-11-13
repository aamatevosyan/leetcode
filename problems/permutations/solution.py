class Solution:
    def helper(self, i: int, nums: List[int], perm: List[int], result: List[List[int]]) -> None:
        if len(perm) == len(nums):
            result.append(perm)
            return
        
        for j in range(len(perm) + 1):
            perm_copy = perm[:]
            perm_copy.insert(j, nums[i])
            self.helper(i + 1, nums, perm_copy, result)

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        self.helper(0, nums, [], result)

        return result
    
        