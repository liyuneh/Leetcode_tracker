class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7

        first = 6
        second = 6

        for _ in range(n - 1):
            next_first = (first * 3 + 2 * second) % mod
            next_second = (2 * first + 2 * second) % mod

            first = next_first
            second = next_second

        return (first + second) % mod