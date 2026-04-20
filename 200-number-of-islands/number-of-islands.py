class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])
        count = 0
        dxn = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def dfs(row, col):
            if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] == "0":
                return 
            grid[row][col] = "0"
            for dx, dy in dxn:
                new_r , new_c = dx + row, dy + col
                dfs(new_r, new_c)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i , j)
        
        return count