class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}

        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        for i in range(len(nums) + 1):
            dp[(i, 0)] = True
        
        # i = how many numbers we’re allowed to use (1-indexed which is why we do nums[i - 1] later)
        # j = the sum we’re trying to make
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if nums[i - 1] <= j:
                    dp[(i, j)] = (
                        dp.get((i - 1, j), False) # Skip it
                        or
                        dp.get((i - 1, j - nums[i - 1]), False) # Take it
                    )
                else: # Only option is too skip it
                    dp[(i, j)] = dp.get((i - 1, j), False)
        
        return dp[(len(nums), target)]