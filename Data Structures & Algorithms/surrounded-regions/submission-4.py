class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                board[r][c] != "O" 
            ):
                return
            
            board[r][c] = "T"
            for dr, dc in moves:
                row, col = r + dr, c + dc
                dfs(row, col)
            

        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1) 

        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c) 
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"