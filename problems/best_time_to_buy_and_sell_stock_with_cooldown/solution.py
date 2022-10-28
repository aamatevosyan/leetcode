class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock, money, prev_money = -math.inf, 0, 0

        for price in prices:
            stock = max(stock, prev_money - price)
            prev_money = money
            
            money = max(stock + price, money)

        return money