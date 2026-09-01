class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_string = len(s1)
        s1 = dict(Counter(s1))
        currentCount = {}

        for r in range(s1_string - 1, len(s2)):
            for i in range(l, r+1):
                currentCount[s2[i]] = currentCount.get(s2[i], 0) + 1
            if currentCount == s1:
                return True
            currentCount.clear()
            l += 1

        return False