class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        if k == 1:
            return r - l + 1
        else:
            a = math.ceil((r) ** ( 1 / k))
            count = 0
            for i in range(int(a) + 1):
                if l <= (i) ** k <= r:
                    count += 1
            return count