class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod = 10 ** 9 + 7
        n = len(pressedKeys)

        dp = [0] * (n + 1)
        dp[0] = 1

        for x in range(n):
            k = int(pressedKeys[x])
            dp[x + 1] = dp[x]
            c = 3
            if k == 7 or k == 9:
                c = 4
            
            for i in range(1,c):
                if x - i < 0 or pressedKeys[x] != pressedKeys[x - i ]:
                    break
                dp[x + 1] += dp[x - i ] 
            dp[x + 1] = dp[x + 1] % mod
        return dp[n]