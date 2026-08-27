class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            newWeight = x - y

            if newWeight != 0:
                heapq.heappush(stones, -newWeight)

        return -stones[0] if stones else 0