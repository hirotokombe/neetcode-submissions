class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            if i >= len(nums):
                return 0

            dp[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))

            return dp[i]
        
        return dfs(0)