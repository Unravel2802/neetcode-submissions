class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        max_area = 0

        def dfs(row, col):
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or 
                grid[row][col] == 0 or
                (row, col) in seen):
                return 0 
            
            seen.add((row, col))
            return (1 + dfs(row + 1, col) + 
                dfs(row - 1, col) + 
                dfs(row, col + 1) + 
                dfs(row, col - 1))
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in seen:
                    max_area = max(max_area, dfs(row, col))
        
        return max_area
        
