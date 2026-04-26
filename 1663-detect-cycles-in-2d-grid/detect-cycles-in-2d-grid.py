import sys
sys.setrecursionlimit(10 ** 7)
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        n , m = len(grid), len(grid[0])
        dxn = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()

        def bound(i, j):return i < 0 or i >= n or j < 0 or j >= m
        
        def dfs(row, col, par):
            temp = grid[row][col]
            visited.add((row, col))
            ans = False
            for dx, dy in dxn:
                ni, nj = row + dx, col + dy
                if bound(ni, nj) or par == (ni, nj) or grid[ni][nj] != temp:continue
                if (ni, nj) in visited:
                    return True
                if dfs(ni, nj , (row, col)):
                    return True
            return ans
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited:
                    if dfs(i, j ,(-1, -1)):
                        return True
        return False
                