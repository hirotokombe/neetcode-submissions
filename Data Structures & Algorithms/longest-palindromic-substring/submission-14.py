class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindrome = ""

        for i in range(len(s)):
            odd = self.helper(s, i, i)
            if len(odd) > len(longestPalindrome):
                longestPalindrome = odd

            even = self.helper(s, i, i + 1)
            if len(even) > len(longestPalindrome):
                longestPalindrome = even

        return longestPalindrome

    def helper(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l + 1:r]

        # When the loop stops, l and r are one step outside the palindrome.
        # l + 1 moves back to the first valid character.
        # r is used directly because Python slicing excludes the end index.
      