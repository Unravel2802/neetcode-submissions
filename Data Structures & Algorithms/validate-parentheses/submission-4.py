class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'}' : '{', ']': '[', ')': '('}

        for ch in s:
            if ch in dic:
                if stack and stack[-1] == dic[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return True if not stack else False