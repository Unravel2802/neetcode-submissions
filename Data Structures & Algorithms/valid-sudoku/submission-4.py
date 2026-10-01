class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        box = [[[] for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if board[i][j] == ".":  
                    continue
                if cell in row[i] or cell in col[j] or cell in box[i//3][j//3]:
                    return False
                
                row[i].append(cell)
                col[j].append(cell)
                box[i//3][j//3].append(cell)
        
        return True