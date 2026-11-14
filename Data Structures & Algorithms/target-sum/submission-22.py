class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, amount):
            if (i, amount) in dp:
                return dp[(i, amount)]
            
            if i == len(nums):
                return 1 if amount == target else 0
            
            dp[(i, amount)] = (
                dfs(i + 1, amount - nums[i]) +
                dfs(i + 1, amount + nums[i])
            )

            return dp[(i, amount)]
        
        return dfs(0, 0)
