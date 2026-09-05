class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        slow, fast = 0, 1
        while slow != fast:
            s_idx = nums[slow]
            slow = s_idx
            
            f1_idx = nums[fast]
            f2_idx = nums[f1_idx]
            fast = f2_idx
    
        return fast
