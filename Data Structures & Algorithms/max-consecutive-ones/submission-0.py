class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentMax = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            if nums[i] == 0 or i == len(nums) - 1:
                if count > currentMax:
                    currentMax = count
                count = 0
        return currentMax

