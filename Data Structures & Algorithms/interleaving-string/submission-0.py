class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ###  Problem Restate: 

        # Given three strings, s1, s2, and s3
        # s3 is like a combination s1 and s2 
        # Return True if s3 is formed by interleaving s1 and s2
        # Interleaving: divide s1 and s2 into m and n substrings, 
        # the difference between m and n is at most 1.
        # AND it needs to look like this: s1 + t1 + s2 + t2 + etc or t1 + s1 + t2 + s2 + etc
        
        ### Questions: 
        # constraints (length of s1, s2, and s3)
        # Does the order of the substring have to stay the same?

        ### Idea:
        # dp[j] means:
        # using current prefix of s1 and first j chars of s2, can we form the needed prefix of s3?
        # Transition:
        # 1. Take next char from s1
        # 2. Take next char from s2


        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False
        
        dp = [False] * (n + 1)
        dp[0] = True

        # First row: only use s2
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            # First column: only use s1
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, n + 1):
                dp[j] = (
                    (dp[j] and s1[i - 1] == s3[i + j - 1]) or
                    (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
                )        

        return dp[n]