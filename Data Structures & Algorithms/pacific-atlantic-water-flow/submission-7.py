class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visitedPac = set()
        visitedAtl = set()

        def dfs(r, c, visited, prevHeight):
            if (
                r not in range(ROWS) or 
                c not in range(COLS) or 
                heights[r][c] < prevHeight or
                (r, c) in visited
            ):
                return
            
            visited.add((r, c))
            for dr, dc in moves:
                row, col = r + dr, c + dc
                dfs(row, col, visited, heights[r][c])

        # Pacific
        for r in range(ROWS):
            dfs(r, 0, visitedPac, heights[r][0]) # Pacific
            dfs(r, COLS - 1, visitedAtl, heights[r][COLS - 1]) # Atlantic

        for c in range(COLS):
            dfs(0, c, visitedPac, heights[0][c]) # Pacific
            dfs(ROWS - 1, c, visitedAtl, heights[ROWS - 1][c]) # Atlantic
            
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visitedPac and (r, c) in visitedAtl:
                    res.append([r, c])
        
        return res