class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time = 0
        fresh = 0 

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1
        
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                
                    if (0 <= new_row < ROWS and
                        0 <= new_col < COLS and
                        grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 2
                        fresh -= 1
                        q.append((new_row, new_col))
            time += 1
        return time if fresh == 0 else -1 