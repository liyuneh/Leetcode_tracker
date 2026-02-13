class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n , m = len(mat), len(mat[0])
        if n <= 2 and m <= 2:
            return [mat[i][j] for i in range(n) for j in range(m)]
        freq = defaultdict(list)
        for i in range(n):
            for j in range(m):
                freq[i + j].append(mat[i][j])
        res = []
        for key , val in freq.items():
            if key % 2 == 0:
                val.reverse()
                res.extend(val)
            else:
                res.extend(val)
        return res