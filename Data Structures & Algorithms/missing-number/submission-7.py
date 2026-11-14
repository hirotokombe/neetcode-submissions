class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Remember that nums is the list that has the missing value so the size is one
        # less than it is supposed to be
        xor = len(nums)
        for i in range(len(nums)):
            xor ^= i ^ nums[i]
        return xor