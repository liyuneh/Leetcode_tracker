class Solution:
    def fib(self, n: int) -> int:
        dp  = [0] * (n +1)
        def fib(n):
            if n == 0 or n == 1:
                return n
            if not dp[n]:
                dp[n] = fib(n - 1) + fib(n  - 2)
            return dp[n]
        return fib(n)