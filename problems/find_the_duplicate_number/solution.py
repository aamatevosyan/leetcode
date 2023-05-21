class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = [False] * (len(nums) + 1)

        for i in range(len(nums)):
            if visited[nums[i]]:
                return nums[i]
            
            visited[nums[i]] = True