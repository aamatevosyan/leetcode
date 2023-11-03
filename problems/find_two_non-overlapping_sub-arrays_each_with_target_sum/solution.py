from collections import defaultdict

class Solution:
    NUM_MAX = float('inf')

    def get_dp_array(self, arr: List[int], target: int) -> List[int]:
        _sum, dp = 0, [self.NUM_MAX] * len(arr)
        num_to_ind = defaultdict(int)

        for i, num in enumerate(arr):
            _sum += num

            if _sum == target:
                dp[i] = i + 1
            elif (_sum - target) in num_to_ind:
                dp[i] = i + 1 - num_to_ind[_sum - target]
            
            num_to_ind[_sum] = i + 1
            dp[i] = min(dp[i - 1], dp[i])
        
        return dp

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        dp_left = self.get_dp_array(arr, target)
        dp_right = self.get_dp_array(arr[::-1], target)[::-1]

        ans = self.NUM_MAX
        for i in range(1, len(arr)):
            ans = min(ans, dp_left[i - 1] + dp_right[i])

        return ans if (ans != self.NUM_MAX) else -1
        