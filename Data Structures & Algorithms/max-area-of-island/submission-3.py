class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or
                grid[row][col] != 1):
                return 0
            
            grid[row][col] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(row + dr, col + dc)
            return area

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))

        return max_area