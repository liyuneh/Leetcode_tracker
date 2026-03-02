class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        # for i in range(len(matrix)):
        #     print(matrix[i])
        self.prefs = [[0] * len(matrix[0]) for _ in range(len(matrix))] 
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                a = self.prefs[i-1][j] if i - 1 >= 0 else 0
                b = self.prefs[i][j-1] if j - 1 >= 0 else 0
                c = self.prefs[i-1][j-1] if i - 1 >= 0 and j - 1 >= 0 else 0
                self.prefs[i][j] = a + b - c + matrix[i][j]
        for i in range(len(self.prefs)):
            print(self.prefs[i])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.prefs[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0
        b = self.prefs[row2][col1-1] if col1 - 1 >= 0 else 0
        c = self.prefs[row1 - 1][col2] if row1 - 1>= 0 else 0
        return self.prefs[row2][col2] - c - b + a

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)