class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Create a dfs function to find the end of an island
        # Use a set to keep track of the land that we already visited
        ROWS, COLS = len(grid), len(grid[0])
        count = 0 

        def dfs(row, col):
            if (row < 0 or row >= ROWS or 
                col < 0 or col >= COLS or 
                grid[row][col] != '1'):
                return
            
            grid[row][col] = 0
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

            return
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    dfs(row, col)
                    count += 1
        
        return count