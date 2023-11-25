class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumped = [True] + [False] * (len(nums) - 1)
        max_reach = 0

        for i in range(len(nums) - 1):
            if not jumped[i]:
                continue

            if nums[i] + i + 1 >= len(nums):
                return True

            if max_reach > nums[i] + i:
                continue

            for j in range(nums[i]):
                jumped[j + i + 1] = True
            
            max_reach = nums[i] + i

        return jumped[-1] 
        