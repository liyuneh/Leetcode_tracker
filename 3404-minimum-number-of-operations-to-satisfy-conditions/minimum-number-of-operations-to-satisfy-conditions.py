class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        dp = [[float('inf')] * 10 for _ in range(m)] 
        ans = [list(new) for new in zip(*grid)]
        for d in range(10):
            dp[0][d] = n - ans[0].count(d)
        # print(dp)

        for col in range(1, m):
            for d in range(10):
                cost = n - ans[col].count(d)

                for prev in range(10):
                    if prev != d:
                        dp[col][d] = min(
                            dp[col][d],
                            dp[col - 1][prev] + cost
                    )
        # print(dp[m-1])
        return min(dp[m - 1])