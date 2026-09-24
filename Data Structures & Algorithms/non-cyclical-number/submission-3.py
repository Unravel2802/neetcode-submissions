class Solution:
    def isHappy(self, n: int) -> bool:
        def cal(n):
            s = 0
            while n > 0:
                digit = n % 10
                s += digit ** 2
                n //= 10
            return s

        slow = n
        fast = cal(n)
        while slow != fast:
            slow = cal(slow)
            fast = cal(fast)
            fast = cal(fast)
        return fast == 1