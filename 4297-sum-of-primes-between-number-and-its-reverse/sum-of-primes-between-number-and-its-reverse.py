class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        def prime(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False

            p = 2
            while p * p <= n:
                if is_prime[p]:
                    for i in range(p * p, n , p):
                        is_prime[i] = False
                p += 1
            ans = [i for i in range(n + 1) if is_prime[i]]
            return ans
        nums = prime(10 ** 5)
        r = int(str(n)[::-1])
        # print(n , r)
        if n > r: n, r = r, n
        x = bisect_left(nums, n)
        y = bisect_right(nums, r)
        return sum(nums[x:y])