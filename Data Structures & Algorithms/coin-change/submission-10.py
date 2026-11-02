class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(i):
            if i == amount:
                return 0
            
            if i > amount:
                return float('inf')
            
            if i in dp:
                return dp[i]
            
            minVal = float('inf')
            for coin in coins:
                minVal = min(minVal, 1 + dfs(i + coin))
            
            dp[i] = minVal
            return dp[i]
    
        numCoins = dfs(0)
        return -1 if numCoins == float('inf') else numCoins