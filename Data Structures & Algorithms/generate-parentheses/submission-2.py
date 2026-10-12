class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = ""
        
        def dfs(openN, closeN):
            nonlocal path

            if openN < n:
                path += '('
                dfs(openN + 1, closeN)
                path = path[:-1]
            
            if closeN < openN:
                path += ')'
                dfs(openN, closeN + 1)
                path = path[:-1]

            if closeN == n:
                res.append(path[:])
            
            return 
    
        dfs(0, 0)
        return res