class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Idea:
        # Start from the end:
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]

        if m == 1 and n == 1:
            return 1
        dp = [[0] * n for _ in range(m)]


        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[m-1][n-1]