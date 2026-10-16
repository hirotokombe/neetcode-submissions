class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i):
            if i == len(nums):
                res.append(nums.copy())
                return
            
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i + 1)
                nums[j], nums[i] = nums[i], nums[j]

        dfs(0)
        return res