class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = [0] * 26
        window = [0] * 26
        left = 0

        for char in s1:
            target[ord(char) - ord('a')] += 1

        for right in range(len(s2)):
            window[ord(s2[right]) - ord('a')] += 1

            if window == target:
                return True

            if right - left + 1 == len(s1):
                window[ord(s2[left]) - ord('a')] -= 1
                left += 1

        return False