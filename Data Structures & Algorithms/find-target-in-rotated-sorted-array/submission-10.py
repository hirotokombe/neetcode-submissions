class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            
        minNum = l
        r = len(nums) - 1
        if target > nums[r]:
            l, r = 0, minNum - 1
            

        while l <= r:
            m = l + (r - l) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1
