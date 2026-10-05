class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def dfs(numOpen, numClosed):
            if numOpen + numClosed == 2 * n:
                string  = "".join(curr)
                res.append(string)
                return
            
            if numOpen < n:
                curr.append("(")
                dfs(numOpen + 1, numClosed)
                curr.pop()
            
            if numClosed < numOpen:
                curr.append(")")
                dfs(numOpen, numClosed + 1)
                curr.pop()
        
        dfs(0, 0)
        return res