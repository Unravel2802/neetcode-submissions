class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def backtrack(row, col, idx):
            if idx == len(word):
                return True
            if (row < 0 or col < 0 or 
                row >= ROWS or col >= COLS or
                board[row][col] != word[idx]):
                return False
            
            temp = board[row][col]
            board[row][col] = '#'

            found = (
                backtrack(row + 1, col, idx + 1) or 
                backtrack(row - 1, col, idx + 1) or 
                backtrack(row, col + 1, idx + 1) or 
                backtrack(row, col - 1, idx + 1)
            )

            board[row][col] = temp
            return found
        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(row, col, 0):
                    return True
        return False