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
        cur = []

        if not digits:
            return []

        def dfs(i):
            if i == len(digits):
                res.append("".join(cur))
                return

            for char in phone[digits[i]]:
                cur.append(char)
                dfs(i + 1)
                cur.pop()

        dfs(0)
        return res