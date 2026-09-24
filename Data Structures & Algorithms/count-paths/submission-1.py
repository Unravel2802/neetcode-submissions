class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Idea:
        # Start from the end:
        # dp[i][j] = dp[i-1][j] + dp[j-1]

        if m == 1 and n == 1:
            return 1
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for r in range(0, m):
            for c in range(0, n):
                if r + c == 1:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        print(dp)
        return dp[m-1][n-1]