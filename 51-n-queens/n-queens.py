class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        ground = [["."] * n for _ in range(n) ]

        def safe(row, col):
            for i in range(row):
                if ground[i][col] == "Q":
                    return False
            r, c = row, col
            while r >= 0 and c >= 0:
                if ground[r][c] == "Q":
                    return False
                r -= 1
                c -= 1
            r, c = row, col
            while r >= 0 and c < n:
                if ground[r][c] == "Q":
                    return False
                r -= 1
                c += 1
            return True
        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in ground])
                return 
            for col in range(n):
                if safe(row, col):
                    ground[row][col] = "Q"
                    backtrack(row + 1)
                    ground[row][col] = "."
        backtrack(0)


        return res