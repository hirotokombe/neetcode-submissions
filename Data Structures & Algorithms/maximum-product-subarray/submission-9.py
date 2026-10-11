class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = curMin = curMax = nums[0]
        for i in range(1, len(nums)):
            oldMax = nums[i] * curMax
            curMax = max(nums[i], curMin * nums[i], oldMax)
            curMin = min(nums[i], curMin * nums[i], oldMax)
       
            maxProd = max(maxProd, curMax)
        return maxProd