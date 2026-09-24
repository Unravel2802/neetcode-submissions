class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 2

        for _ in range(n - 1):
            temp = one
            one = two
            two = one + temp
        
        return one