class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for num in nums:
            curSum  = max(num + curSum, num)
            maxSub = max(maxSub, curSum)
        return maxSub