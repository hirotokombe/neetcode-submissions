class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        map = {}
        maxLength = 0
        length = 0
        for r in range(len(s)):
            if s[r] in map:
                l = max(map[s[r]] + 1, l)
            maxLength = max(maxLength, r - l + 1)
            map[s[r]] = r
        return maxLength
        