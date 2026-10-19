class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((t, v))
        
        t = 0
        visited = set()
        minHeap = [(0, k)]

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)

            if n1 in visited:
                continue
            
            visited.add(n1)
            t = t1

            for t2, n2 in adj[n1]:
                if n2 in visited:
                    continue
                heapq.heappush(minHeap, (t1 + t2, n2))
        
        return t if len(visited) == n else -1
