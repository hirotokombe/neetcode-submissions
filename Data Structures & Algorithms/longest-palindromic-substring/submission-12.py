class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            l = r = i
            currentPalindrome = self.helper(s, l, r)
            if len(currentPalindrome) > len(longest):
                longest = currentPalindrome

            currentPalindrome = self.helper(s, l, r + 1)
            if len(currentPalindrome) > len(longest):
                longest = currentPalindrome
        return longest

    def helper(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l + 1:r]