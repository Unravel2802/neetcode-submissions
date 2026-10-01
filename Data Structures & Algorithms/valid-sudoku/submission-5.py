class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if board[r][c] == ".":  
                    continue
                if (cell in row[r] or 
                    cell in col[c] or 
                    cell in box[(r//3,c//3)]):
                    return False
                
                row[r].add(cell)
                col[c].add(cell)
                box[(r//3, c//3)].add(cell)
        
        return True