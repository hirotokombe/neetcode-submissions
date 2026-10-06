class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        moves = [[1, 0], [-1, 0], [0, 1],[0, -1]]

        visited = set()
        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visited or
                board[r][c] != word[idx]
            ):
                return False



            visited.add((r, c))
            idx += 1 

            for dr, dc in moves:
                row, col = dr + r, dc + c
                if dfs(row, col, idx):
                    return True
            visited.remove((r, c))
            
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        
        return False
                    
