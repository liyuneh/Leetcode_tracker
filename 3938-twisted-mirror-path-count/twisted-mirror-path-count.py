class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        Mod = 10 ** 9 + 7
        n , m = len(grid), len(grid[0])
        dp = [[[0,0] for _ in range(m)]  for _ in range(n)]
        dp[0][0][0] = 1
        for i in range(n):
            for j in range(m):
                if i > 0:
                    if grid[i - 1][j] == 0:
                        dp[i][j][0] = dp[i - 1][j][0] + dp[i-1][j][1]
                    else:
                        dp[i][j][0] = dp[i-1][j][1]
                    dp[i][j][0] %= Mod
                if j > 0:
                    if grid[i][j - 1] ==  0:
                        dp[i][j][1] = dp[i][j-1][0] + dp[i][j-1][1]
                    else:
                        dp[i][j][1] = dp[i][j-1][0]
                    dp[i][j][1]%= Mod
                

        return sum(dp[n-1][m-1]) % Mod       