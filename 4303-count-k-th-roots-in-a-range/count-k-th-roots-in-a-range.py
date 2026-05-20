class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        if k == 1:
            return r - l + 1
        else:
            a = math.ceil((r) ** ( 1 / k))
            print(a)
            count = 0
            for i in range(int(a) + 1):
                print(i)
                if l <= (i) ** k <= r:
                    count += 1
            print(count)
            return count