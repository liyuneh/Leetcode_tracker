class Solution:
    def findGCD(self, nums: list[int]) -> int:
        nums.sort()
        return math.gcd(nums[0], nums[-1])