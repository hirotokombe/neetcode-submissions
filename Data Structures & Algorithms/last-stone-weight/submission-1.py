class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            newWeight = y - x

            if newWeight != 0:
                heapq.heappush(heap, newWeight)
        
        return -heap[0] if heap else 0