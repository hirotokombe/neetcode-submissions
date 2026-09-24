class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        maxArea = 0
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= ROW or c >= COL or
                grid[r][c] == 0
            ):
                return 0
            
            count = 1 if grid[r][c] == 1 else 0
            grid[r][c] = 0

            for dr, dc in moves:
                count += dfs(r + dr, c + dc)
            
            return count
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)
        
        return maxArea
