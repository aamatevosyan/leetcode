class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumped = [False] * len(nums)
        jumped[0] = True

        for i, jump in enumerate(nums):
            if not jumped[i]:
                continue
            
            end = min(i + jump + 1, len(nums))
            if end >= len(nums):
                return True

            for j in range(i + 1, min(i + jump + 1, len(nums))):
                jumped[j] = True
        
        return jumped[-1]
