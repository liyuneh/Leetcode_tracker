class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3)* 3 + (j // 3)].add(val)
        
        def backtrack(r,c):
            if r == 9 :
                return True

            if board[r][c] != ".":
                if c < 8:
                    return backtrack(r, c + 1)
                else:
                    return backtrack(r + 1, 0)

            bx = (r // 3) * 3 + (c // 3)
            for num in map(str, range(1, 10)):
                if num not in rows[r] and num not in cols[c] and num not in boxes[bx]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[bx].add(num)
                    if c < 8:
                        if backtrack(r, c + 1):
                            return True
                    else:
                        if backtrack(r + 1, 0):
                            return True

                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[bx].remove(num)
        backtrack(0,0)