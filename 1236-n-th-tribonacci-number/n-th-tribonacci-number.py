class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {}
        def memo(i):
            if i == 0:
                return 0
            if i <= 2:
                return 1
            if i not in dp:
                dp[i] = memo(i - 1) + memo(i - 2 ) + memo(i-3)
            return dp[i]
        return memo(n)
            