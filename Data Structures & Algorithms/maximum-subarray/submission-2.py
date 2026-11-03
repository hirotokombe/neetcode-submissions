class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSub, maxSub = 0, nums[0]
        for num in nums:
            curSub = max(num, curSub + num)
            maxSub = max(maxSub, curSub)
        
        return maxSub