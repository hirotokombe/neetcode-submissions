class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {
            0: True
        }

        for i in range(1, len(s) + 1):
            for word in wordDict:
                dp[i] = False
                if (
                    i - len(word) >= 0 and 
                    s[i - len(word) : i] == word and 
                    dp[i - len(word)]
                ):
                    dp[i] = True
                    break

        return dp[len(s)]