class Solution:
    def climbStairs(self, n: int) -> int:
        l , r = 0 , 1
        for i in range(n):
            l , r = r , r + l
        return r