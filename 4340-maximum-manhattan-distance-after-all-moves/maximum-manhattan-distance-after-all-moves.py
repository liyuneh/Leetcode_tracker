class Solution:
    def maxDistance(self, moves: str) -> int:
        u,d,l,r = 0, 0, 0 ,0
        ans = 0
        for x in moves:
            if x == "U":
                u += 1
            elif x == "D":
                d += 1
            elif x == "R":
                r += 1
            elif x == "L":
                l += 1
            else:
                ans += 1
        new = ans + abs(u - d) + abs(l - r)
        return new