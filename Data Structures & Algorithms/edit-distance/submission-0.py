class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Idea:
        # dp[i][j]
        # if i < j and word[i] != word[j], we choose to add character/delete character
        # if i == j, we replace chracter? but does it matter which operation we choose?
        # keep track of the next characters?
        # if the next characters are equal, then we insert

        m, n = len(word1), len(word2)
        diff = abs(m - n)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][n] = m - i

        for j in range(n + 1):
            dp[m][j] = n - j

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    insert_op = dp[i][j + 1]
                    delete_op = dp[i + 1][j]
                    replace_op = dp[i + 1][j + 1]

                    dp[i][j] = 1 + min(insert_op, delete_op, replace_op)         

        return dp[0][0]
