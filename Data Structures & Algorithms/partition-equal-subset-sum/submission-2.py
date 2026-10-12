class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}

        total = sum(nums)
        if total % 2 != 0:
            return False
    
        target = total // 2
        def dfs(i, target):
            if (i, target) in dp:
                return dp[(i, target)]
            
            if target == 0:
                return True
            
            if i >= len(nums) or target < 0:
                return False
            
            dp[(i, target)] = (
                dfs(i + 1, target) or
                dfs(i + 1, target - nums[i])
            )
            return dp[(i, target)]
     


        
        return dfs(0, target)