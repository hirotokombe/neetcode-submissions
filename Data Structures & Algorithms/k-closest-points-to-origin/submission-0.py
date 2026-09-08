class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []

        for point in points:
            distance = (0 - point[0]) ** 2 + (0 - point[1])**2
            heapq.heappush(closest, (-distance, point))
            if len(closest) > k:
                heapq.heappop(closest)

        return [heapq.heappop(closest)[1] for _ in range(len(closest))]