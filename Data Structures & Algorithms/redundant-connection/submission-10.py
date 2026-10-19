class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        cycle = set()
        def dfs(node, parent):
            if node in visited:
                return True, node

            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                
                isCycle, cycleStart = dfs(neighbor, node)
                if isCycle:
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
                
