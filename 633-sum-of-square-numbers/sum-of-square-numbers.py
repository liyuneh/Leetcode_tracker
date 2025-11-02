class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l , r = 0, int(math.sqrt(c))
        while l <= r:
            Sum = l * l + r * r
            if Sum == c:
                return True
            elif Sum < c:
                l += 1
            else:
                r -= 1
        return False