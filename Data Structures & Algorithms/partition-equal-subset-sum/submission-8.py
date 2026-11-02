class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        dp = {}

        target = sum(nums) // 2
        def dfs(i, amount):
            if (i, amount) in dp:
                return dp[(i, amount)]

            if i >= len(nums) and amount != target:
                return False

            if amount == target:
                return True



            dp[(i, amount)] = (
                dfs(i + 1, amount) or
                dfs(i + 1, amount + nums[i])
            )

            return dp[(i, amount)]
        
        return dfs(0, 0)