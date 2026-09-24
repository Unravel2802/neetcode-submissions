class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_alnum = ""
        i = 0 
        for ch in s:
            if ch.isalnum():
                s_alnum += ch
                
        left = 0
        right = len(s_alnum)-1
        print(s_alnum)
        while left < right:
            if s_alnum[left] != s_alnum[right]:
                return False
            left += 1
            right -= 1
        return True