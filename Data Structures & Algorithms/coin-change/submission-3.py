class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(i):
            if i == amount:
                return 0
            if i in dp:
                return dp[i]
            if i > amount:
                return float("inf")
            minCoins = float("inf")
            for coin in coins:
                minCoins = min(minCoins, 1 + dfs(i + coin))
            
            dp[i] = minCoins
            return dp[i]
            
        numCoins = dfs(0)

        return -1 if numCoins == float("inf") else numCoins
