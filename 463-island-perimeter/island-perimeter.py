class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        n , m = len(grid), len(grid[0])
        dxn = [(-1,0),(0,-1), (1,0), (0,1)]
        def dfs(r,c):
            if r < 0 or r >= n or c < 0 or c >= m :
                return 1
            if grid[r][c] == 0:
                return 1
            if grid[r][c] == -1:
                return 0
            grid[r][c] = -1
            per = 0
            for dx, dy in dxn:
                per += dfs(dx + r, dy + c)
            return per
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs(i, j)