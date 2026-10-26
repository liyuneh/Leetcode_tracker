class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n , m = len(grid), len(grid[0])
        dxn = [(1,0), (0,1),(-1,0),(0,-1)]
        def inbound(i, j) : return 0 <= i < n and 0 <= j < m
        def dfs(i, j):
            if not inbound(i, j) or grid[i][j] == 0:
                return 0
            cnt =  grid[i][j]
            grid[i][j] = 0
            for dx , dy in dxn:
                nr, nc = i + dx, j + dy
                cnt += dfs(nr,nc)
            return cnt
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    ans = dfs(i, j)
    
                    if ans % k == 0:
                        count += 1
        # print(count)
        return count
