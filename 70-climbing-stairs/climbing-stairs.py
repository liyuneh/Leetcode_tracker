class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * ( n + 1)
        def new (n):
            if  dp[n]:
                return dp[n]
            if n < 3:
                return n
            dp[n] = new(n - 1) + new(n - 2)
            return dp[n]
        return new(n) 