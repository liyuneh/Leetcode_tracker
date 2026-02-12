class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(matrix[0])):
            ans = []
            for j in range(len(matrix)):
                ans.append(matrix[j][i])
            res.append(ans)
        # print(res)
        return res