class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        dp = {0: True}

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = (
                    dp.get(j, False)              # Skip num
                    or
                    dp.get(j - num, False)        # Take num
                )

        return dp.get(target, False)