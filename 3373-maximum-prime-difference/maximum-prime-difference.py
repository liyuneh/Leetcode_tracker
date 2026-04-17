class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(n):
            if n < 2:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while  i * i <= n:
                if n % i == 0 or n % ( i + 2) == 0:
                    return False
                i += 6
            return True
        prev = -1
        for i in range(len(nums)):
            if is_prime(nums[i]):
                prev = i
                break
        if prev == -1:
            return -1
        for i in range(len(nums)- 1, -1, -1):
            if is_prime(nums[i]):
                return i - prev
