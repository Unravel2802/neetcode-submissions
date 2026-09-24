class Solution:
    def isHappy(self, n: int) -> bool:
        # 1 -> finite
        # 2 -> infinite
        # 3 9 81 65 61 37 -> infinite
        # 4 16 37 -> infinite
        # 5 25 29 85 89 -> infinite
        # 6 36 45 41 17 50 -> infinite
        # 7 49 97 130 -> finite
        # 8 64 52 29 -> infinite
        # 9 81 -> infinite
        def cal(n):
            s = 0
            while n > 0:
                digit = n % 10
                s += digit**2
                n = n // 10
            return s

        cyclical = [2, 3, 4, 5, 6, 8, 9]

        while True:
            s = cal(n)
            if s in cyclical:
                return False
            elif s == 1 or s == 7: 
                return True
            else:
                n = s