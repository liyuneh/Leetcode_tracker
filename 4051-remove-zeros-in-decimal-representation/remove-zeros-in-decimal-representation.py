class Solution:
    def removeZeros(self, n: int) -> int:
        ans = []
        while n > 0:
            rem = n % 10
            if rem != 0:
                ans.append(rem)
            n //= 10
        ans.reverse()
        return int("".join(map(str, ans)))