class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()

        def dfs(row, col):
            if (row < 0 or col < 0 or 
                row >= ROWS or col >= COLS or
                grid[row][col] == "0" or
                (row, col) in seen):
                return 
            
            seen.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)            
            
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in seen:
                    dfs(row, col)
                    count += 1
        
        return count