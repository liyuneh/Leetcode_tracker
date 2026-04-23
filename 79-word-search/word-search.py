class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n , m = len(board), len(board[0])
        dxn = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(row, col, k):
            if k == len(word):
                return True
            if row < 0 or row >= n or col < 0 or col >= m or board[row][col] != word[k]:
                return False
            temp = board[row][col]
            board[row][col] = "#"
            for x, y in dxn:
                if dfs(row + x, col + y,k + 1):
                    return True
            board[row][col] = temp
            return False
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False