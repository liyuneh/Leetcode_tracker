class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [["#" for _ in range(n)] for _ in range(m)]
        # for i in range(n)

        for i in range(m):
            grid[i][0] = "."
        for i in range(n):
            grid[m - 1][i] = "."
        ans = []
        for i in range(m):
            ans.append("".join(grid[i]))
        
        return ans