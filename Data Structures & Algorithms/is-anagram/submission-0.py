class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        if len(s) != len(t):
            return False
        
        for charS, charT in zip(s, t):
            dict1[charS] = dict1.get(charS, 0) + 1
            dict2[charT] = dict2.get(charT, 0) + 1
        
        return dict1 == dict2

            
            
