class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(x ** 2 if len(nums) % (i + 1) == 0 else 0 for i, x in enumerate(nums))