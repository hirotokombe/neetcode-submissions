class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
        return max(dp[i] for i in range(len(nums)))