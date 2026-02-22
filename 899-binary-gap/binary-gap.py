class Solution:
    def binaryGap(self, n: int) -> int:
        mn = 0
        x = bin(n)[2:]
        l = x.index("1")
        r = l + 1
        while r < len(x):
            if x[r] == x[l]:
                mn = max(mn ,abs(l - r))
                l = r
            r += 1
        print(mn)

        return mn