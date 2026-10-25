class Solution:
    """
    Returns the minimum number of edits needed to turn word1[i:] into word2[j:].

    We do NOT actually modify the strings; we simulate each operation
    by deciding which pointer(s) move forward:

    - Delete word1[i]  -> move i forward:     dfs(i + 1, j)
    - Insert word2[j]  -> move j forward:     dfs(i, j + 1)
    - Replace word1[i] -> move both forward:  dfs(i + 1, j + 1)

    Each simulated edit costs 1 operation, so after choosing the
    cheapest future path, we add 1.
    """
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        
        def dfs(i, j):
            # word1 is finished, so insert every remaining character from word2.
            if i == len(word1):
                return len(word2) - j

            # word2 is finished, so delete every remaining character from word1.
            if j == len(word2):
                return len(word1) - i
            if (i, j) in dp:
                return dp[(i, j)]
                
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                res = min(dfs(i + 1, j), dfs(i, j + 1)) # DELETE word1[i] and INSERT word2[j]
                res = min(res, dfs(i + 1, j + 1))  # REPLACE word1[i] with word2[j]
                dp[(i, j)] = res + 1
            return dp[(i, j)]

        return dfs(0, 0)
            
