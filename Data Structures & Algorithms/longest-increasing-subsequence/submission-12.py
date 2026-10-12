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
    
        # If nums[j] can come after nums[i],
        # 1 counts nums[i] and dfs(j) finds the best chain from nums[j].
        #
        # Use max because different valid j choices can lead
        # to different subsequence lengths, so keep the longest one found.