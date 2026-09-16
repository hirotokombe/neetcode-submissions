class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
    
        for idx, val in enumerate(nums):
            difference = target - val
            if difference in dict:
                return [dict[difference], idx]
            
            dict[val] = idx
        
        return None