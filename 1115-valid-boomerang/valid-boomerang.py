class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        res = []
        ans = []
        for x, y in points:
            res.append(x)
            ans.append(y)
        x1, x2, x3 = res
        y1, y2, y3 = ans
        return (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)
