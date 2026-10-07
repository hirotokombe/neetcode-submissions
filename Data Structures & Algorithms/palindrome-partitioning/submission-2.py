class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def dfs(i):
            if i == len(s):
                res.append(cur.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    cur.append(s[i:j + 1])
                    dfs(j + 1)
                    cur.pop()

        def isPalindrome(l, r) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True
        
        dfs(0)
        return res