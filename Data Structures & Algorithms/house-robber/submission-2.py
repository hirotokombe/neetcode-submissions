class Solution:
    def rob(self, nums: List[int]) -> int:
        cache =  [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return cache[i]

        return dfs(0)
 # The i + 2 part is not just “rob the house two away”; it means after robbing i, the next place we’re allowed to consider is i + 2, and dfs(i + 2) figures out the best possible amount from there onward.