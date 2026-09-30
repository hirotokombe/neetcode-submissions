class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque([])
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
                    
        dist = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                for dr, dc in moves:
                    row, col = r + dr, c + dc
                    if (
                        row not in range(ROWS) or
                        col not in range(COLS) or
                        (row, col) in visited or
                        grid[row][col] == -1
                    ):
                        continue
                    
                    queue.append((row, col))
                    visited.add((row, col))
        
            dist += 1

                
