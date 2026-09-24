class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1 
        two = 2

        for i in range(n - 1):
            temp = one
            one = two
            two = one + temp
        
        return one