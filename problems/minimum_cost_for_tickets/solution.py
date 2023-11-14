class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        dp = [0] * (last_day + 1)

        i = 0
        for cur_day in range(last_day + 1):
            if cur_day < days[i]:
                dp[cur_day] = dp[cur_day - 1]
                continue
            
            dp[cur_day] = min(
                dp[cur_day - 1] + costs[0],
                dp[max(0, cur_day - 7)] + costs[1],
                dp[max(0, cur_day - 30)] + costs[2] 
            ) 
            i += 1
        
        return dp[-1]
            


        