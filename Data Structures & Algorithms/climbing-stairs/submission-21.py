class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def dfs(i):
            if i >= n:
                return i == n

            if i in dp:
                return dp[i]

            dp[i] = dfs(i + 1) + dfs(i + 2)
            return dp[i]

        return dfs(0)
