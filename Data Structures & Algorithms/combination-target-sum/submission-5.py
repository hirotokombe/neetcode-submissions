class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()

        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
            
            for j in range(i, len(nums)):
                if nums[j] + total > target:
                    return
                curr.append(nums[j])
                dfs(j, total + nums[j])
                curr.pop()
        
        dfs(0, 0)
        return res