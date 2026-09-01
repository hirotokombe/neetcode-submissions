class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        target_alphabet = [0] * 26
        current_alphabet = [0] * 26
        target_length = len(s1)

        for i in s1:
            index = ord(i) - ord('a')
            target_alphabet[index] += 1

        for right in range(len(s2)):
            index = ord(s2[right]) - ord('a')
            current_alphabet[index] += 1

            if current_alphabet == target_alphabet:
                return True

            if len(s2[left:right + 1]) == target_length:
                index = ord(s2[left]) - ord('a')
                current_alphabet[index] -= 1
                left += 1

        return False
