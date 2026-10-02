class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        target = [0] * 26
        current = [0] * 26

        for i in range(len(s1)):
            s1_index = ord(s1[i]) - ord('a')
            target[s1_index] += 1

            s2_index = ord(s2[i]) - ord('a')
            current[s2_index] += 1

        matches = 0
        for i in range(26):
            if target[i] == current[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                break; 
        
            index = ord(s2[r]) - ord('a')
            current[index] += 1
            if target[index] == current[index]:
                matches += 1
            if target[index] + 1 == current[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            current[index] -= 1
            if target[index] == current[index]:
                matches += 1
            if target[index] - 1 == current[index]:
                matches -= 1
            
            l += 1

        return matches == 26 