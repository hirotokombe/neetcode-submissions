class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

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