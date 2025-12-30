class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def isMagic(r: int, c: int) -> bool:
            nums = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if grid[i][j] < 1 or grid[i][j] > 9:
                        return False
                    nums.add(grid[i][j])

            if len(nums) != 9:
                return False

            for i in range(3):
                if sum(grid[r + i][c:c + 3]) != 15:
                    return False
                if grid[r][c + i] + grid[r + 1][c + i] + grid[r + 2][c + i] != 15:
                    return False

            if (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15 or
                grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15):
                return False

            return True

        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagic(i, j):
                    count += 1

        return count
