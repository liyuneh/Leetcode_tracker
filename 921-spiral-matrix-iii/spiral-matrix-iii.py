class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        total = rows * cols

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        r, c = rStart, cStart
        step = 1

        if 0 <= r < rows and 0 <= c < cols:
            result.append([r, c])

        while len(result) < total:
            for d in range(4):
                dr, dc = directions[d]

                for _ in range(step):
                    r += dr
                    c += dc

                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                        if len(result) == total:
                            return result

                if d == 1 or d == 3:
                    step += 1

        return result
        