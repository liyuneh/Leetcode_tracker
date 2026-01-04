class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def is_prime(n):
            if n < 2:
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
        Sum = 0
        for num in nums:
            count = 2
            inner_sum = 1 + num
            if num < 4:
                continue
            if is_prime(num):
                continue
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    index = num // i
                    count += 1
                    inner_sum += i
                    if i != index :
                        count += 1
                        inner_sum += index
                    if count > 4:
                        break
            if count == 4:
                Sum += inner_sum

            
        return Sum