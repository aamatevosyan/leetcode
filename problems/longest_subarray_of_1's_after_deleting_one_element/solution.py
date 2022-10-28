class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt, prev_cnt, ans = 0, 0, 0

        for j in range(len(nums)):
            if nums[j] == 1:
                cnt += 1
            else:
                prev_cnt = cnt
                cnt = 0
            
            ans = max(ans, prev_cnt + cnt)
        
        return ans - 1 if ans == len(nums) else ans