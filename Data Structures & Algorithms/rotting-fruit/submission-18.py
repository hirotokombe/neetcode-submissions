class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        freshCount = 0
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        minutes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshCount += 1
                    
 
        while freshCount > 0:
            rottedThisMinute = False
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        for dr, dc in moves:
                            row, col = r + dr, c + dc
                            if (
                                row in range(ROWS) and 
                                col in range(COLS) and 
                                grid[row][col] == 1
                            ):
                                rottedThisMinute = True
                                freshCount -= 1
                                grid[row][col] = 3
            
            if not rottedThisMinute:
                return -1
          
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 3:
                        grid[r][c] = 2

            minutes += 1
            
        return minutes


    