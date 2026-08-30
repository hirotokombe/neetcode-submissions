class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for i in range(len(strs)):
            alphabet = [0] * 26
            for char in strs[i]:
                alphabet[ord(char) - ord('a')] += 1
            anagram[tuple(alphabet)].append(strs[i])
        
        return list(anagram.values())
