class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = float('inf')
        for price in prices:
            maxProfit = max(maxProfit, price - minBuy)
            minBuy = min(minBuy, price)
        
        return maxProfit