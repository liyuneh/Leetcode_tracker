class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        def primes(n):
            is_prime = [True] * ( n + 1)
            is_prime[0] = is_prime[1] = False

            i = 2
            while i * i <= n:
                if is_prime[i]:
                    for j in range(i * i, n + 1, i ):
                        is_prime[j] = False
                i += 1
            prime = []
            for i in range(2, n + 1):
                if is_prime[i]:
                    prime.append(i)
            return prime
        ans = primes(2 * (10 ** 5))

        count = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                if not is_prime(nums[i]):
                    count += (ans[bisect_right(ans, nums[i])] - nums[i])
            else:
                if is_prime(nums[i]):
                    if nums[i] == 2:
                        count += 2
                    else:
                        count += 1
        print(count)
        return count 
                    