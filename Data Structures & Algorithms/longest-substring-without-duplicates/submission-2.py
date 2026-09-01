class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        right = 0
        longest = 0
        for i in range(len(s)):
            if s[i] in seen:
                while s[left] != s[i]:
                    seen.discard(s[left])
                    left += 1
                left += 1
            seen.add(s[i])
            longest = max(longest, len(seen))
        return longest
