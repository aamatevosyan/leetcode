class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = math.inf
        maxProfit = 0

        for price in prices:
            maxProfit = max(maxProfit, price - minPrice)
            
            if price < minPrice:
                minPrice = price
        
        return maxProfit