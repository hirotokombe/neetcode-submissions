class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            LIS = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                   LIS = max(LIS, 1 + dfs(j))   
            dp[i] = LIS
            return dp[i]

        return max(dfs(i) for i in range(len(nums)))