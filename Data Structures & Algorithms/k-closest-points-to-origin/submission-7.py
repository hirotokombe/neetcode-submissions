class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for point in points:
            euc_dist = (0 - point[0]) ** 2 + (0 - point[1]) ** 2
            heapq.heappush(heap, (-euc_dist, point))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(len(heap))]
