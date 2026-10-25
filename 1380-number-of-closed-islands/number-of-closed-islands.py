class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n , m = len(grid), len(grid[0])
        dxn = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def inbound(i, j) : return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        def dfs(i, j):
            grid[i][j] = 1
            for dx, dy in dxn:
                nr, nc = i + dx, j + dy
                if inbound(nr, nc) and  grid[nr][nc] == 0:
                    dfs(nr, nc)

        for i in range(n):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][m - 1] == 0:
                dfs(i, m - 1)
        for i in range(m):
            if grid[0][i] == 0:
                dfs(0 , i)
            if grid[n - 1][i] == 0:
                dfs(n - 1, i)
        cnt = 0           
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    cnt += 1
                    dfs(i, j)
       
        return cnt