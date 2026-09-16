class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        if len(s) != len(t):
            return False
            
        for i, j in zip(s, t):
            dict1[i] = dict1.get(i, 0) + 1
            dict2[j] = dict2.get(j, 0) + 1
        
        return dict1 == dict2