class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = []
        opens = []

        for i, c in enumerate(s):
            if c == '(':
                opens.append(i)
            elif c == '*':
                stars.append(i)
            
            else:
                if opens:
                    opens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        
        while opens and stars:
            if opens[-1] > stars[-1]:
                return False
            opens.pop()
            stars.pop()
        
        return not opens