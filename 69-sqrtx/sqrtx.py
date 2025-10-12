class Solution:
    def mySqrt(self, x: int) -> int:
        left , right = 0, x
        while left <= right:
            mid = (left + right)//2
            m_square = mid * mid
            if m_square == x:
                return mid
            elif m_square < x:
                left = mid + 1
            else:
                right = mid - 1
        return right