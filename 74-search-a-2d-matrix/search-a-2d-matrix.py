class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m , n = len(matrix), len(matrix[0])

        left , right = 0, m*n- 1

        while left <= right:
            middle = (left + right) // 2
            i , j = divmod(middle, n)
            value = matrix[i][j]
            if value == target:
                return True
            elif value < target:
                left = middle + 1
            else:
                right = middle - 1
        return False