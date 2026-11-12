class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, canBuy):
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]

            if i >= len(prices):
                return 0

            skip = dfs(i + 1, canBuy)
            if canBuy:
                weBuy = dfs(i + 1, not canBuy) - prices[i]
                dp[(i, canBuy)] = max(skip, weBuy)
            else:
                weSell = dfs(i + 2, not canBuy) + prices[i]
                dp[(i, canBuy)] = max(skip, weSell)
            
            return dp[(i, canBuy)]
        
        return dfs(0, True)
