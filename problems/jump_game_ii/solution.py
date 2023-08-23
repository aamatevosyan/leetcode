class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_ind, max_ind, jumps = 0, 0, 0
        
        for i in range(len(nums) - 1):
            max_ind = max(max_ind, i + nums[i])

            if i == cur_ind:
                cur_ind = max_ind
                jumps += 1

        return jumps
        

