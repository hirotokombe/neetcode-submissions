class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        res = []
        curr = []

        if not digits:
            return []

        def dfs(i):
            if i == len(digits):
                string = "".join(curr.copy())
                res.append(string)
                return
            
            for char in phone[digits[i]]:
                curr.append(char)
                dfs(i + 1)
                curr.pop()
            
        dfs(0)
        return res