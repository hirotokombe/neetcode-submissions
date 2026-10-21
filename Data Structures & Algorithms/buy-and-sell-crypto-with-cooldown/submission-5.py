class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0] → can sell
        # dp[i][1] → can buy
        dp = [[0] * 2 for _ in range(len(prices) + 1)]

        for i in range(len(prices) - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy, cooldown = -prices[i], 0 

                    if i + 1 < len(prices):
                        buy = dp[i + 1][False] - prices[i]
                        cooldown = dp[i + 1][True] 

                    dp[i][1] = max(buy, cooldown)
                else:
                    sell, cooldown = prices[i], 0 
                    if i + 2 < len(prices):
                        sell = dp[i + 2][True] + prices[i]
                    if i + 1 < len(prices):
                        cooldown = dp[i + 1][False]
                    
                    dp[i][0] = max(sell, cooldown)
        
        return dp[0][1]

