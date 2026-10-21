class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp[r][c] = the total number of unique paths to get to that cell
        # transitions:
        # if no obstacle dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
        # if obstacle dp[r][c] = 0
    
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0]  * (cols + 1) for _ in range(rows + 1)]

        if obstacleGrid[rows - 1][cols -1] == 1:
            return 0

        dp[rows - 1][cols - 1] = 1

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                elif r != rows - 1 or c != cols - 1:
                    dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
        return dp[0][0]