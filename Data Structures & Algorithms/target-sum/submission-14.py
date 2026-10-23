class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp is a list of dictionaries.
        # Each dp[i] represents the totals we can make after using the first i numbers.
        #
        # Inside each dictionary:
        # key   = a possible total
        # value = how many different +/- choices create that total
        #
        # defaultdict(int) means any missing total automatically starts at 0,
        # which is useful because we can safely do: dp[i][total] += count
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(len(nums)):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count
        
        return dp[len(nums)][target]

