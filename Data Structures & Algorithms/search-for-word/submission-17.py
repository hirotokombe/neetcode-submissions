class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(i, r, c):
            if i == len(word):
                return True
            
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                board[r][c] != word[i] or
                (r, c) in visited
            ):
                return False

            visited.add((r, c))
            i += 1
            for dr, dc in moves:
                row, col = r + dr, c + dc
                if dfs(i, row, col):
                    return True
            
            visited.discard((r, c))

            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(0, r, c):
                    return True
        
        return False
            