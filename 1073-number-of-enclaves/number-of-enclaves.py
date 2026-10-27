class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        n , m = len(grid), len(grid[0])
        dxn = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def inbound(i, j): return 0 <= i < n and 0 <= j < m

        def dfs(i, j):
            if not inbound(i,j) or grid[i][j] == 0:
                return 
            grid[i][j] = 0

            for dx, dy in dxn:
                nr, nc = i + dx, j + dy
                dfs(nr,nc)
        
        for i in range(n):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][m - 1] == 1:
                dfs(i, m - 1)
        for i in range(m):
            if grid[0][i] == 1:
                dfs(0 , i)
            if grid[n - 1][i] == 1 :
                dfs(n - 1, i)
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt += 1
        # print(cnt)
        return cnt