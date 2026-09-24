class Solution:
    def longestPalindrome(self, s: str) -> str:
        # idea: A palindrome expands from its center
        # For each index:
        # 
        res_r, res_l = 0, 0
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return l + 1, r - 1
        
        for i in range(len(s)):
            l1, r1 = expand(i, i)
            if r1 - l1 > res_r - res_l:
                res_l, res_r = l1, r1
            
            l2, r2 = expand(i, i + 1)
            if r2 - l2 > res_r - res_l:
                res_l, res_r = l2, r2

        return s[res_l : res_r + 1]