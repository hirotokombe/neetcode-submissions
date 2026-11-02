class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            odd = self.helper(s, i, i)
            if len(odd) > len(longest):
                longest = odd

            even = self.helper(s, i, i + 1)
            if len(even) > len(longest):
                longest = even
        
        return longest

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        return s[l + 1:r]