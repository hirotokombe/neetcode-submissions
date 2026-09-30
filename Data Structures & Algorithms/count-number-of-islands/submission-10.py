class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0

        def dfs(r, c):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] == "0"
            ):
                return
            
            grid[r][c] = "0"
            for dr, dc in moves:
                row, col = r + dr, c + dc
                dfs(row, col)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        
        return islands