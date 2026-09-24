class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check for rows 
        # check for columns
        for i in range(9):
            check_row = set()
            check_col = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in check_row:
                    return False
                if board[j][i] != "." and board[j][i] in check_col:
                    return False
                check_row.add(board[i][j])
                check_col.add(board[j][i])

        # check for 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                check_box = set()
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        if board[r][c] != "." and board[r][c] in check_box:
                            return False
                        check_box.add(board[r][c])
        return True
