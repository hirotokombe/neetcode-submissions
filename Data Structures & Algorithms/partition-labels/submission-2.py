class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastLetter = {}
        for i, v in enumerate(s):
            lastLetter[v] = i
        
        res = []
        start = end = 0
        for i, v in enumerate(s):
            end = max(end, lastLetter[v])
            if i == end:
                res.append(len(s[start:end + 1]))
                start = end + 1
        
        return res