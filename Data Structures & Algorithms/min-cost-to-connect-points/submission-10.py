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
        
        visited = set()
        minHeap = [(0, 0)]
        cost = 0
        while len(visited) < len(points):
            c1, n1 = heapq.heappop(minHeap)

            if n1 in visited:
                continue
            
            visited.add(n1)
            cost += c1

            for c2, n2 in adj[n1]:
                if n2 in visited:
                    continue
                heapq.heappush(minHeap, (c2, n2))
            
        return cost 


