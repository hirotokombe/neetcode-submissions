class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
            
            for j in range(i, len(candidates)):
                
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] + total > target:
                    return
                curr.append(candidates[j])
    
                dfs(j + 1, total + candidates[j])
                curr.pop()
        
        dfs(0, 0)
        return res