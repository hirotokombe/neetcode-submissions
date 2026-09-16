class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        map = defaultdict(list)
        for word in strs:
            alphabet = [0] * 26
            for char in word:
                letter = ord(char) - ord('a')
                alphabet[letter] += 1
            
            map[tuple(alphabet)].append(word)
        
        return list(map.values())