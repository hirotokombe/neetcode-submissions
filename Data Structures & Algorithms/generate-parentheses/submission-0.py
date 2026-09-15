class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        def dfs(openCount, closedCount):
            if len(cur) == (n * 2):
                combo = "".join(cur)
                res.append(combo)
                return

            if openCount < n:
                cur.append("(")
                dfs(openCount + 1, closedCount)
                cur.pop()
            
            if closedCount < openCount:
                cur.append(")")
                dfs(openCount, closedCount + 1)
                cur.pop()
        
        dfs(0, 0)
        return res
