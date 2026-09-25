class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Start BFS from all treasure cells (0) at the same time.
        # Each BFS layer represents cells that are 1 step farther from the nearest treasure.
        # The first time a cell is reached, that distance is guaranteed to be the shortest.
        # Mark it visited so another treasure's BFS cannot overwrite it with a longer distance.
            
        ROWS, COLS = len(grid), len(grid[0])
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque([])
        visited = set()

        # Find the teasure first
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        
        
        def bfs(q, dist):
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
            
                    grid[r][c] = dist
                    for dr, dc in moves:
                        row, col = r + dr, c + dc
                        if (
                            row not in range(ROWS) or 
                            col not in range(COLS) or
                            grid[row][col] == -1 or
                            (row, col) in visited

                        ):
                            continue

                        q.append((row, col))
                        visited.add((row, col))

                dist += 1
        

        bfs(queue, 0)

