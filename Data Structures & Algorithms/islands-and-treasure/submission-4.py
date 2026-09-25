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
        
        
        def bfs(q, dist):
            while q:
                for _ in range(len(q)):
                    cell = q.popleft()
                    r, c = cell[0], cell[1]

                    grid[r][c] = dist
                    for dr, dc in moves:
                        if (
                            r + dr < 0 or c + dc < 0 or
                            r + dr >= ROWS or c + dc >= COLS or
                            grid[r + dr][c + dc] == -1 or
                            (r + dr, c + dc) in visited

                        ):
                            continue

                        q.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))

                dist += 1
        

        bfs(queue, 0)

