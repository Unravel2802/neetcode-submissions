class Solution:
    def isHappy(self, n: int) -> bool:
        def cal(n):
            s = 0
            while n > 0:
                digit = n % 10
                s += digit ** 2
                n //= 10
            return s

        seen = set()

        while n not in seen:
            seen.add(n)
            if n == 1:
                return True
            n = cal(n)
        return False