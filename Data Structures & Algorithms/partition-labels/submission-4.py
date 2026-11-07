class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSpot = {}
        for i, v in enumerate(s):
            lastSpot[v] = i
        
        end = start = 0
        res = []
        for i, v in enumerate(s):
            end = max(end, lastSpot[v])
            if i == end:
                res.append(len(s[start:end + 1]))
                start = end + 1
        return res