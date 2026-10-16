class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []

        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(candidates)):            
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                if total + candidates[j] > target:
                    return
 
                curr.append(candidates[j])
                dfs(j + 1, total + candidates[j])

                curr.pop()
            
        dfs(0, 0)
        return res

