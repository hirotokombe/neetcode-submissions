class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        res = 0
        visit = set()
        minHeap = [(0, 0)]

        while len(visit) < len(points):
            cost, idx = heapq.heappop(minHeap)
            if idx in visit:
                continue

            res += cost
            visit.add(idx)
            for dist, neighbor in adj[idx]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, (dist, neighbor))
            
        return res

                        
