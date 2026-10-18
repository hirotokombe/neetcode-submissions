class Solution:
    # Build an undirected adjacency list.

    # DFS marks every node in one connected component as visited.

    # If the outer loop finds an unvisited node,
    # that means it starts a new component.

    # Run DFS from it and increase the component count by 1.
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        componentCount = 0

        def dfs(node):
            visit.add(node)
            for neighbor in adj[node]:
                if neighbor not in visit:
                    dfs(neighbor)
        
        for node in range(n):
            if node not in visit:
                componentCount += 1
                dfs(node)

        
        return componentCount