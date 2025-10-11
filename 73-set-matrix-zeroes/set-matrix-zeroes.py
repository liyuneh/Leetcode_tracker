class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows = set()
        zero_col = set()
        for i in range(len(matrix)):
            for  j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_col.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_rows or j in zero_col:
                    matrix[i][j] = 0     