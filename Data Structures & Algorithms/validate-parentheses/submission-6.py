class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mp:
                if stack and mp[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
    
        return True if not stack else False
