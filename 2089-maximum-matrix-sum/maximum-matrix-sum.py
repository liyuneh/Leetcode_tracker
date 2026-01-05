class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        count = 0
        mn = float('inf')
        total = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] < 0:
                    count += 1
                mn = min(mn, abs(matrix[i][j]))
                total += abs(matrix[i][j])

        if count % 2 == 0:
            return total
        else:
            return total - 2 * mn
