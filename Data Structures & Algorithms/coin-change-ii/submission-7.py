class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = {}
        # amount + 1 because we nned every amount from 0 to amount
        # len(coins) + 1 because we need one extra row for the state where we've
        # gone past the last coin (matches the base case)

        def dfs(i, a):
            if a == 0:
                return 1
            
            # run out of coin types to try while there’s still some amount left, 
            # so that path cannot form the target
            if i >= len(coins):
                return 0
            
            if (i, a) in dp:
                return dp[(i, a)]
            
            res = 0
            if a >= coins[i]:
                res = dfs(i + 1, a)
                res += dfs(i, a - coins[i])
            
            dp[(i, a)] = res
            return res
        
        return dfs(0, amount)
