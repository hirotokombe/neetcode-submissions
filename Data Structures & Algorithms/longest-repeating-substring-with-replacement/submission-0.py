class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) +  1

            subwindow_length = r - l + 1
            most_frequent = max(count.values())
            replaceable = subwindow_length - most_frequent

            if replaceable <= k:
                longest = max(longest, subwindow_length)
            else:
                count[s[l]] -= 1
                l += 1
                
        return longest
