class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dic = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        res = []
        path = ""
        def dfs(idx):
            nonlocal path

            if len(path) == len(digits):
                res.append(path[:])
                return
            
            for j in range(idx, len(digits)):
                for c in dic[digits[j]]:
                    path += c 
                    dfs(j + 1)
                    path = path[:-1]

        dfs(0)
        return res

