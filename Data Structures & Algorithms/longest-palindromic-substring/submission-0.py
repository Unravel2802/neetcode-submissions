class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        # idea: Brute force: 
        # start with max_len = 1 and up to max_len = len(s)
        # check if each substring from i to i + max_len is palindrome

        max_sub = s[0]
        for max_len in range(len(s)):
            for i in range(len(s) - max_len):
                if isPalindrome(i, i + max_len):
                    max_sub = s[i : i + max_len + 1]
        
        return max_sub
        
