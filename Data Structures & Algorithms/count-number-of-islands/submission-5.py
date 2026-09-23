class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROW, COL = len(grid), len(grid[0])
        islands = 0
        def dfs(r, c):
            if (
                r < 0 or
                c < 0 or
                r >= ROW or
                c >= COL or
                grid[r][c] == "0"
            ):
                return
            
            grid[r][c]  = "0"

            for dr, dc in moves:
                dfs(r + dr, c + dc)
            
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands
            
