class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n , m = len(board), len(board[0])
        dxn = [(-1,0), (1, 0), (0, 1), (0, -1)]
        def dfs(row, col):
            if row < 0 or row >=  n or col < 0 or col >= m or board[row][col] != "O":
                return 
            board[row][col] = "a"
            for x, y in dxn:
                dfs(row + x, col + y)
            
        for i in range(n):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][m - 1] == "O":
                dfs(i, m - 1)
        for i in range(m):
            if board[0][i] == "O":
                dfs(0 , i)
            if board[n - 1][i] == "O":
                dfs(n - 1, i)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] ="X"
                if board[i][j] == "a":
                    board[i][j] = "O"
