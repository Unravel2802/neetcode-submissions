class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c in dic:
                if not stack or dic[c] != stack[-1]:
                    return False 
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        return not stack