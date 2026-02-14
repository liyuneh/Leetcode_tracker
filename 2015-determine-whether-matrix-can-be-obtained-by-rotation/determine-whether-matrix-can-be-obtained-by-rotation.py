class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            for i in range(len(mat)):
                for j in range(i , len(mat)):
                    mat[i][j] ,mat[j][i] = mat[j][i], mat[i][j]
            print(mat)
            for row in mat:
                row.reverse()
            if mat == target :
                return True

        return False