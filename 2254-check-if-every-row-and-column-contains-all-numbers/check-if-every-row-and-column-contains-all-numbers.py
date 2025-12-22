class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        num = [i for i in range(1,n+1)]
        print(num)
        transpose = []
        for i in range(n):
            ans = []
            for  j in range(len(matrix[i])):
                ans.append(matrix[j][i])
            transpose.append(ans)
        as_it_is  = True
        transposed = True
        for  i in range(n):
            if sorted(matrix[i]) != num:
                as_it_is = False
                break
            if sorted(transpose[i]) != num:
                transposed = False
                break

        return as_it_is and transposed