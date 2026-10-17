class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Start from point 0 and build the MST one node at a time.
        # For each newly visited node, check its distance to every unvisited point.
        # Update dist[i] with the cheapest connection found from any visited node to point i.
        # Select the unvisited point with the smallest dist[i] and add its cost to the MST.
        # Repeat until all points are connected.
        node = 0
        dist = [float('inf')] * len(points)
        visit = set()
        edges, res = 0, 0

        while edges < len(points) - 1:
            visit.add(node)
            nextNode = None

            for i in range(len(points)):
                if i in visit:
                    continue

                x1, y1 = points[node][0], points[node][1]
                x2, y2 = points[i][0], points[i][1]
                currentDistance = abs(x1 - x2) + abs(y1 - y2)
                dist[i] = min(dist[i], currentDistance)
                if nextNode is None or dist[i] < dist[nextNode]:
                    nextNode = i # This keeps track of the node's idx that gives us the min distance
            
            res += dist[nextNode]
            node = nextNode
            edges += 1

        return res 
                
                
