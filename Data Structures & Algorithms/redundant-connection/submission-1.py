class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        cycle = set()

        def dfs(node, parent):
            if node in visit:
                return True, node

            visit.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue

                foundCycle, cycleStart = dfs(nei, node)

                if foundCycle:
                    if cycleStart != -1:
                        cycle.add(node)

                    if node == cycleStart:
                        cycleStart = -1

                    return True, cycleStart

            return False, -1

        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []