class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = 0
        while l <= r:
            m = (r + l) // 2
            total = 0
            for pile in piles:
                time = math.ceil(pile / m)
                total += time
            
            if total > h:
                l = m + 1
            else:
                best = m
                r = m - 1
        
        return best