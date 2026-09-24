class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                box_key = (r//3, c//3)
                if board[r][c] == '.':
                    continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[box_key]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(box_key)].add(board[r][c])

        return True  