class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n , m = len(grid), len(grid[0])
        dxn = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(row, col):
            if col < 0 or col >= m  or row < 0 or row >= n:
                return 1
            if grid[row][col] == 0:
                return 1
            if grid[row][col] == -1:
                return 0

            grid[row][col] = -1
            per = 0
            for x, y in dxn:
                per += dfs(row + x, col + y)
            return per

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs(i, j)