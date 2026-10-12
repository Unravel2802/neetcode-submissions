class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []
        def isPalindrome(s):
            return s == s[::-1]

        def dfs(idx):
            if idx == len(s):
                res.append(path[:])
                return
            
            for j in range(idx, len(s)):
                sub = s[idx : j + 1]
                if not isPalindrome(sub):
                    continue
                
                path.append(sub)
                dfs(j + 1)
                path.pop()

        dfs(0)
    
        return res