class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxLength = 0
        dict = {}
    
        for r in range(len(s)):
            dict[s[r]] = dict.get(s[r], 0) + 1

            while ((r - l + 1) - max(dict.values())) > k:
                dict[s[l]] -= 1
                l += 1 
            
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength