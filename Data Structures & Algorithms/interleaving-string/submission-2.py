class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = {}
        def dfs(i, j, k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            
            # k does not need to be stored because k is always equal to i + j.
            # If we know i and j, we automatically know our position in s3.
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = dfs(i + 1, j, k + 1)
            if not res and j < len(s2) and s2[j] == s3[k]:
                res = dfs(i, j + 1, k + 1)
            
            dp[(i, j)] = res
            return res
        
        return dfs(0, 0, 0)
