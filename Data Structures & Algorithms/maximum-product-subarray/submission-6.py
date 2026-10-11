class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = curMin = curMax = nums[0]
        for i in range(1, len(nums)):
            tmpMax = max(nums[i], curMin * nums[i], curMax * nums[i])
            tmpMin = min(nums[i], curMin * nums[i], curMax * nums[i])
            curMax, curMin = tmpMax, tmpMin
            maxProd = max(maxProd, curMax)
        return maxProd