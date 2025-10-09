class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        k = abs(x)
        result = 0
        while k > 0:
            result = 10 * result + k % 10
            k //= 10
        result *= sign 
        if result < -2**31  or result > 2**31 - 1:
            return 0
        return result
        