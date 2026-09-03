class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, sum(piles)
        curr_min = 0
        while l <= r:
            full_time = 0
            k = (l + r) // 2
            for pile in piles:
                time = math.ceil(pile / k)
                full_time += time
            
            if full_time <= h:
                r = k - 1
                curr_min = k
            elif full_time > h:
                l = k + 1
        return curr_min