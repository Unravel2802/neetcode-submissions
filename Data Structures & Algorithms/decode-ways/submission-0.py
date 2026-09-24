class Solution:
    def numDecodings(self, s: str) -> int:
        # Idea:
        # Let dp[i] = number of ways to decode the prefix of s[:i]
        # At each position, we can:
        # 1. Decode one digit if s[i-1] != '0'
        # 2. Decode two digits if s[i-2:i] is between 10 and 26

        n = len(s)
        if s[0] == '0':
            return 0
        
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
    
        for i in range(2, n + 1):
            # One digit decode:
            if s[i-1] != '0':
                dp[i] += dp[i - 1]
            
            two = int(s[i-2:i])
            if 10 <= two <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]