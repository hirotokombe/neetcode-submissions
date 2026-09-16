class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = [0] * 26
        window = [0] * 26

        # Build the first window
        for i in range(len(s1)):
            target[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        # Count how many of the 26 letters currently match
        matches = 0
        for i in range(26):
            if target[i] == window[i]:
                matches += 1

        left = 0

        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Add new character on the right
            index = ord(s2[right]) - ord('a')
            window[index] += 1

            if window[index] == target[index]:
                matches += 1
            elif window[index] == target[index] + 1:
                matches -= 1

            # Remove old character on the left
            index = ord(s2[left]) - ord('a')
            window[index] -= 1

            if window[index] == target[index]:
                matches += 1
            elif window[index] == target[index] - 1:
                matches -= 1

            left += 1

        return matches == 26