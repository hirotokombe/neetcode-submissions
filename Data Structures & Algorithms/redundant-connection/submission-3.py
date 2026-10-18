class Solution:
    # Build an undirected adjacency list.

    # DFS through the graph while keeping track of the parent
    # so we do not mistake the edge back to the parent for a cycle.

    # If DFS reaches a node that was already visited,
    # that node is where the cycle begins.

    # As recursion returns back up, add each node on that path
    # to the cycle set until we reach the cycle's starting node again.

    # Finally, scan the edges backwards and return the last edge
    # whose two endpoints are both part of the detected cycle.
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        cycle = set()

        def dfs(node, parent):
            if node in visit:
                return True, node

            visit.add(node)

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue

                foundCycle, cycleStart = dfs(neighbor, node)

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