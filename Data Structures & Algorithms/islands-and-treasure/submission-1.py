class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))
        
        INF = 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if (0 <= new_row < ROWS and
                    0 <= new_col < COLS and
                    grid[new_row][new_col] == INF):
                    grid[new_row][new_col] = grid[row][col] + 1
                    q.append((new_row, new_col))