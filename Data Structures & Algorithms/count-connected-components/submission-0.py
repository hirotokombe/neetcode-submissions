class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = [False] * n
        componentCount = 0

        def dfs(node):
            for neighbor in adj[node]:
                if not visit[neighbor]:
                    visit[neighbor] = True
                    dfs(neighbor)
        
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                componentCount += 1
                dfs(node)

        
        return componentCount