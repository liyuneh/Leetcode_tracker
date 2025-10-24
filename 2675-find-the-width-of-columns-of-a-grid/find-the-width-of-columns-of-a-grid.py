class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = []
        if not grid:
            return []

        def transpose(grid: List[List[int]]) -> List[List[int]]:
            rows = len(grid)
            cols = len(grid[0])
            transposed = [[0 for _ in range(rows)] for _ in range(cols)]
            for i in range(rows):
                for j in range(cols):
                    transposed[j][i] = grid[i][j]
            return transposed

        z = transpose(grid)

        for c in range(len(z)):
            res = 0
            for j in range(len(z[c])):
                res = max(res, len(str(z[c][j])))
            ans.append(res)
        
        return ans