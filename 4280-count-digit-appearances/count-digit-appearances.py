class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        ans = 0
        for i in range(len(nums)):
            k = str(nums[i])
            if str(digit) in k:
                b = k.count(str(digit))
                ans += b
        return ans