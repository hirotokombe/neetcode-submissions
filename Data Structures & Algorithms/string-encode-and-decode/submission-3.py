class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append('#')
            res.append(word)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        while j < len(s):
            while s[j] != '#':
                j += 1 
            length = int(s[i:j])
            i = j + 1
            j = i + length
            word = s[i:j]
            res.append(word)
            i = j
        return res
            