class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def dfs(i):
            # Reaching the end means the whole string was successfully segmented.
            if i == len(s):
                return True

            if i in dp:
                return dp[i]

            for word in wordDict:
                if s[i : i + len(word)] == word:
                    if dfs(i + len(word)):
                        dp[i] = True
                        return True

            dp[i] = False
            return False

        return dfs(0)