class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charNum = {}
        maxLength = 0
        l = 0
        for r in range(len(s)):
            charNum[s[r]] = charNum.get(s[r], 0) + 1
            
            while (r - l + 1) - max(charNum.values()) > k:
                charNum[s[l]] -= 1
                l += 1
            
            maxLength = max(maxLength, (r - l + 1))
    
        return maxLength


