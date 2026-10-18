Mod = 10 ** 9 + 7
fact = [1, 1]
ifact = [1, 1]

for i in range(2, 1005):
    fact.append((fact[-1] * i) % Mod)
    ifact.append(pow(fact[-1], -1, Mod))


class Solution:
    def numOfWays(self, nums: list[int]) -> int:

        def dfs(arr):
            n = len(arr)

            if n <= 1:
                return 1

            pivot = arr[0]
            left, right = [], []

            for x in arr[1:]:
                if x < pivot:
                    left.append(x)
                else:
                    right.append(x)

            lres = dfs(left)
            rres = dfs(right)

            l = len(left)
            r = len(right)

            c = (fact[l + r] * ifact[l] * ifact[r]) % Mod

            return (lres * rres * c) % Mod

        return (dfs(nums) - 1) % Mod