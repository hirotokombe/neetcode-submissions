class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = curMin = curMax = nums[0]
        for i in range(1, len(nums)):
            oldMax = nums[i] * curMax
            newMax = max(nums[i], curMin * nums[i], oldMax)
            newMin = min(nums[i], curMin * nums[i], oldMax)
            curMax, curMin = newMax, newMin
            maxProd = max(maxProd, curMax)
        return maxProd