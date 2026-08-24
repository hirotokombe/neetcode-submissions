class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k) 
                # Round up because any partially eaten pile (which would be shown as a decimal) still takes a full hour.
            if totalTime <= h:
                res = k # this saves the current slowest speed (aka the minimum)
                r = k - 1
            else:
                l = k + 1
        return res