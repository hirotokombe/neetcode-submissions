class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        numSet = set(nums)
        for num in nums:
            if num - 1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                maxLength = max(maxLength, length)
        
        return maxLength
