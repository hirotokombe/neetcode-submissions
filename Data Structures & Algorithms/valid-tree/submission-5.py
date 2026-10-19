class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n

