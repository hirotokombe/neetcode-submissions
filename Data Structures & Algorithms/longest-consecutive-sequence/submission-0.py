class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in nums:
                i = 1
                length = 1
                while num + i in nums:
                    length += 1
                    i += 1
                longest = max(longest, length)
            
        
        return longest
