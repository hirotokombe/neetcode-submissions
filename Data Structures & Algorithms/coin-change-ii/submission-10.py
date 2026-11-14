class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, a):
            if (i, a) in dp:
                return dp[(i, a)]
            
            if a == amount:
                return 1
            
            if a > amount or i == len(coins):
                return 0 
                
            dp[(i, a)] = (
                dfs(i + 1, a) +
                dfs(i, a + coins[i])
            )
            
            return dp[(i, a)]

        return dfs(0, 0)