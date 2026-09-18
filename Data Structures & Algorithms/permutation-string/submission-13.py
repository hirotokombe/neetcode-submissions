class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        target = [0] * 26
        window = [0] * 26

        for i in range(len(s1)):
            s1Letter = ord(s1[i]) - ord('a')
            target[s1Letter] += 1

            s2Letter = ord(s2[i]) - ord('a')
            window[s2Letter] += 1

        match = 0
        for i in range(len(target)):
            if window[i] == target[i]:
                match += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            
            if match == 26:
                return True

            index = ord(s2[r]) - ord('a')
            window[index] += 1

            if window[index] == target[index]:
                match += 1
            elif window[index] == target[index] + 1:
                match -= 1
            
            index = ord(s2[l]) - ord('a')
            window[index] -= 1
            if window[index] == target[index]:
                match += 1
            elif window[index] == target[index] - 1:
                match -= 1
            l+= 1

        return match == 26
            