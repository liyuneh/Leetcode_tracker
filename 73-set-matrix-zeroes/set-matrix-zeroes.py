class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        vertical_zeros = set()
        horizental_zeros = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    horizental_zeros.add(i)
                    vertical_zeros.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in horizental_zeros or j in vertical_zeros:
                    matrix[i][j] = 0
        