class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if ((r == 0 or r == rows - 1 
                    or c == 0 or c == cols - 1) and 
                    board[r][c] == "O"):
                    q.append((r, c))

        safe = set()

        while q:
            r, c = q.popleft()

            if (r, c) in safe:
                continue
            
            safe.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and
                    0 <= nc < cols and 
                    (nr, nc) not in safe and
                    board[nr][nc] == "O"):
                    q.append((nr, nc))
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in safe:
                    board[r][c] = "X"
        

