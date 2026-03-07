class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        n = len(grid)
        flag = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] not in seen:
                    seen.add(grid[i][j])
                else:
                    flag = grid[i][j]
        for i in range(1, n ** 2 + 1):
            if i not in seen:
                return [flag , i]