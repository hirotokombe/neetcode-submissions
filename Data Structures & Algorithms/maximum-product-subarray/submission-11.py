class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minVal = maxVal = maxProd = nums[0]

        for i in range(1, len(nums)):
            currMax = nums[i] * maxVal
            maxVal = max(nums[i], maxVal * nums[i], minVal * nums[i])
            minVal = min(nums[i], currMax, minVal * nums[i])
            maxProd = max(maxProd, maxVal)
        
        return maxProd