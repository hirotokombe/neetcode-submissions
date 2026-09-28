class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        adj = [[] for _ in range(n)]

        for u, v in edges:
            # we add it to both u and v because the graph is undirected
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
                
        
        return dfs(0, -1) and len(visit) == n
        
