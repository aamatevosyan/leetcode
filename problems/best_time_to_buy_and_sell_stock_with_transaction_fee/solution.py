class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold, notHold = -math.inf, 0

        for price in prices:
            hold = max(hold, notHold - price)
            notHold = max(notHold, price + hold - fee)
        
        return notHold
        

